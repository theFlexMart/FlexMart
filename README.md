# FlexMart
Serveless ecommerce solution built on top of AWS

## setup environment
install (pulumi cli)[https://www.pulumi.com/docs/install/]
setup aws cli. to do that you can follow (this document)[https://www.pulumi.com/registry/packages/aws-native/installation-configuration/] 
use python version manager of your choice eg: pyenv, venv etc.

set `PYTHONPATH` on the root of this repo
```sh
export PYTHONPATH=.
```

select stack
```sh
pulumi stack select
```

run `pulumi up` for deployment
