"""An Azure Python Pulumi program"""

import pulumi
import pulumi_azure as azure
from createdby import username

config = pulumi.Config()

# Please correctly fill in the vars below - these vars are used to create tags
created_by = username()
team = "Dev Team"
scope = "ICAP Project"
port_num = "1344"

# To do - write functions for the below variables
rg = "gw-icap-performance-pool-c11c167a"
im = "glasswallicap58de6aa8.azurecr.io/test-icap:v0.1"
acrserver = "glasswallicap58de6aa8.azurecr.io"

create_container_instance = azure.containerservice.Group("glasswallicap-1-",
    location="UKSouth",
    resource_group_name=f"{rg}",
    ip_address_type="public",
    dns_name_label="icapdns1",
    os_type="Linux",
    image_registry_credentials=[
        azure.containerservice.GroupImageRegistryCredentialArgs(
            server=f"{acrserver}",
            username=config.require_secret('acrusername'),
            password=config.require_secret('acrpassword'),
        )],
    containers=[
        azure.containerservice.GroupContainerArgs(
            name="icap-test",
            image=f"{im}",
            cpu=1,
            memory=1.5,
            ports=[azure.containerservice.GroupContainerPortArgs(
                port="{port_num}"
                protocol="TCP",
            )],
        )],
        tags={
            "Created by": f"{created_by}",
            "Team": f"{team}",
            "Scope": f"{scope}"
        })

create_container_instance = azure.containerservice.Group("glasswallicap-2-",
    location="UKSouth",
    resource_group_name=f"{rg}",
    ip_address_type="public",
    dns_name_label="icapdns2",
    os_type="Linux",
    image_registry_credentials=[
        azure.containerservice.GroupImageRegistryCredentialArgs(
            server=f"{acrserver}",
            username=config.require_secret('acrusername'),
            password=config.require_secret('acrpassword'),
        )],
    containers=[
        azure.containerservice.GroupContainerArgs(
            name="icap-test",
            image=f"{im}",
            cpu=1,
            memory=1.5,
            ports=[azure.containerservice.GroupContainerPortArgs(
                port="{port_num}"
                protocol="TCP",
            )],
        )],
        tags={
            "Created by": f"{created_by}",
            "Team": f"{team}",
            "Scope": f"{scope}"
        })

create_container_instance = azure.containerservice.Group("glasswallicap-3-",
    location="UKSouth",
    resource_group_name=f"{rg}",
    ip_address_type="public",
    dns_name_label="icapdns3",
    os_type="Linux",
    image_registry_credentials=[
        azure.containerservice.GroupImageRegistryCredentialArgs(
            server=f"{acrserver}",
            username=config.require_secret('acrusername'),
            password=config.require_secret('acrpassword'),
        )],
    containers=[
        azure.containerservice.GroupContainerArgs(
            name="icap-test",
            image=f"{im}",
            cpu=1,
            memory=1.5,
            ports=[azure.containerservice.GroupContainerPortArgs(
                port="{port_num}"
                protocol="TCP",
            )],
        )],
        tags={
            "Created by": f"{created_by}",
            "Team": f"{team}",
            "Scope": f"{scope}"
        })

create_container_instance = azure.containerservice.Group("glasswallicap-4-",
    location="UKSouth",
    resource_group_name=f"{rg}",
    ip_address_type="public",
    dns_name_label="icapdns4",
    os_type="Linux",
    image_registry_credentials=[
        azure.containerservice.GroupImageRegistryCredentialArgs(
            server=f"{acrserver}",
            username=config.require_secret('acrusername'),
            password=config.require_secret('acrpassword'),
        )],
    containers=[
        azure.containerservice.GroupContainerArgs(
            name="icap-test",
            image=f"{im}",
            cpu=1,
            memory=1.5,
            ports=[azure.containerservice.GroupContainerPortArgs(
                port="{port_num}"
                protocol="TCP",
            )],
        )],
        tags={
            "Created by": f"{created_by}",
            "Team": f"{team}",
            "Scope": f"{scope}"
        })

create_container_instance = azure.containerservice.Group("glasswallicap-5-",
    location="UKSouth",
    resource_group_name=f"{rg}",
    ip_address_type="public",
    dns_name_label="icapdns5",
    os_type="Linux",
    image_registry_credentials=[
        azure.containerservice.GroupImageRegistryCredentialArgs(
            server=f"{acrserver}",
            username=config.require_secret('acrusername'),
            password=config.require_secret('acrpassword'),
        )],
    containers=[
        azure.containerservice.GroupContainerArgs(
            name="icap-test",
            image=f"{im}",
            cpu=1,
            memory=1.5,
            ports=[azure.containerservice.GroupContainerPortArgs(
                port="{port_num}"
                protocol="TCP",
            )],
        )],
        tags={
            "Created by": f"{created_by}",
            "Team": f"{team}",
            "Scope": f"{scope}"
        })
