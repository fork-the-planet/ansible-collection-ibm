
ibm_is_private_path_service_gateway_endpoint_gateway_binding_info -- Retrieve IBM Cloud 'ibm_is_private_path_service_gateway_endpoint_gateway_binding' resource
===============================================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_private_path_service_gateway_endpoint_gateway_binding' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_private_path_service_gateway_endpoint_gateway_binding

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  private_path_service_gateway (True, str, None)
    The private path service gateway identifier.


  endpoint_gateway_binding (True, str, None)
    The endpoint gateway binding identifier.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

