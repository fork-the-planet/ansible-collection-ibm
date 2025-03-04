
ibm_pi_network_port_attach -- Configure IBM Cloud 'ibm_pi_network_port_attach' resource
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_network_port_attach' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_network_port_attach

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  pi_instance_id (True, str, None)
    (Required for new resource) Instance id to attach the network port to


  pi_network_port_description (False, str, Port Created via Terraform)
    A human readable description for this network Port


  pi_user_tags (False, list, None)
    The user tags attached to this resource.


  pi_cloud_instance_id (True, str, None)
    (Required for new resource)


  pi_network_name (True, str, None)
    (Required for new resource) Network Name - This is the subnet name  in the Cloud instance


  pi_network_port_ipaddress (False, str, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  zone (False, str, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environment variable 'IC_ZONE'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

