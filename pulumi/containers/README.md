# Pulumi Container Deployment

## Setting up venv and pip packages

Assuming you have virtualenv installed (if you don't please follow this [link](https://pypi.org/project/virtualenv/1.7.1.2/#:~:text=You%20can%20install%20virtualenv%20with,it%20with%20python%20virtualenv.py.)) follow the below commands to get the packages installed

## Setting up Pulumi

Cd into "pulumi/registry" then use the following commands to initiate the stack and set the correct secrets.

```bash
pulumi stack select ACR_Stack

pulumi config set --secret acrusername <enter acr username>

pulumi config set --secret acrpassword <enter acr password>
```

ACR username and password can be found on the registry itself (glasswallicap58de6aa8) under "Access Keys".

Once the secrets provider has been set, you can then use the following command and respond yes to the prompt pulumi provides.

```bash
pulumi up

Previewing update (ACR_Stack):
     Type                   Name                  Plan
     pulumi:pulumi:Stack    ACR_Deploy-ACR_Stack
     └─ docker:image:Image  test-icap

Resources:
    4 unchanged

Permalink: https://stpulumi.blob.core.windows.net/pulumi/.pulumi/stacks/ACR_Stack.json?se=2020-09-28T13%3A04%3A22Z&sig=6MzIgXJZRiq8wJzq65ecxjT9xP%2B6gIR0IoJxacf161o%3D&sp=r&spr=https&sr=b&sv=2018-11-09
Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
  yes
> no
  details
```

## Notes about "createdby.py" function

This function was added to take the name of the person who is initialising this Pulumi deployment and add it to the tags sections of the code. This is so AppSec are aware of who is deploying what.

If it is giving you any issues please give me a message on slack or email mpigram@glasswallsolutions.com



## Notes about "createdby.py" function

This function was added to take the name of the person who is initialising this Pulumi deployment and add it to the tags sections of the code. This is so AppSec are aware of who is deploying what.

If it is giving you any issues please give me a message on slack or email mpigram@glasswallsolutions.com