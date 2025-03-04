#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_volumes_info
for_more_info: refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_volumes

short_description: Retrieve IBM Cloud 'ibm_is_volumes' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_is_volumes' resource
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    volume_name:
        description:
            - Volume name identifier.
        required: False
        type: str
    zone_name:
        description:
            - Zone name identifier.
        required: False
        type: str
    attachment_state:
        description:
            - Attachment state of the Volume.
        required: False
        type: str
    encryption:
        description:
            - Encryption type of Volume.
        required: False
        type: str
    operating_system_family:
        description:
            - Operating system family of the Volume.
        required: False
        type: str
    operating_system_architecture:
        description:
            - Operating system architecture of the Volume.
        required: False
        type: str
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
        type: str
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'volume_name',
    'zone_name',
    'attachment_state',
    'encryption',
    'operating_system_family',
    'operating_system_architecture',
]


TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    volume_name=dict(
        required=False,
        type='str'),
    zone_name=dict(
        required=False,
        type='str'),
    attachment_state=dict(
        required=False,
        type='str'),
    encryption=dict(
        required=False,
        type='str'),
    operating_system_family=dict(
        required=False,
        type='str'),
    operating_system_architecture=dict(
        required=False,
        type='str'),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    if 'generation' in module.params:
        # VPC required arguments checks
        if module.params['generation'] == 1:
            missing_args = []
            if module.params['iaas_classic_username'] is None:
                missing_args.append('iaas_classic_username')
            if module.params['iaas_classic_api_key'] is None:
                missing_args.append('iaas_classic_api_key')
            if missing_args:
                module.fail_json(msg=(
                    "VPC generation=1 missing required arguments: " +
                    ", ".join(missing_args)))
        elif module.params['generation'] == 2:
            if module.params['ibmcloud_api_key'] is None:
                module.fail_json(
                    msg=("VPC generation=2 missing required argument: "
                         "ibmcloud_api_key"))

    result = ibmcloud_terraform(
        resource_type='ibm_is_volumes',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
