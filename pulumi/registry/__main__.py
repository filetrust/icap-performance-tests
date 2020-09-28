"""An Azure Python Pulumi program"""

import pulumi
import pulumi_docker
import pulumi_azure as azure
from pulumi_azure import core, containerservice
from createdby import username

# Please correctly fill in the vars below - these vars are used to create tags
created_by = username()
team = "Dev Team"
scope = "ICAP Project"

# Creates resource group and adds tags from vars above
resource_group = azure.core.ResourceGroup("gw-icap-performance-pool-", location="UKSouth",
        tags={
            "Created by": f"{created_by}",
            "Team": f"{team}",
            "Scope": f"{scope}"
        })

# Create registry
registry = containerservice.Registry('glasswallicap',
    admin_enabled=True,
    sku='Standard',
    resource_group_name=resource_group.name,
        tags={
            "Created by": f"{created_by}",
            "Team": f"{team}",
            "Scope": f"{scope}"
        })

# ImageRegistry
r = pulumi.Output.all(registry.login_server,
    registry.admin_username,
    registry.admin_password).apply(
        lambda a: pulumi_docker.ImageRegistry(a[0], a[1], a[2])
    )

# Build and Publish image
image = pulumi_docker.Image("test-icap",
    image_name=registry.login_server.apply(lambda s: f'{s}/test-icap:v0.1'),
    build=pulumi_docker.DockerBuild(context='./c-icap'),
    registry=r,)
