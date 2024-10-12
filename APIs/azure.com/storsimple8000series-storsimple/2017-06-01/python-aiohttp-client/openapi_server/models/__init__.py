# coding: utf-8

# import models into model package
from openapi_server.models.access_control_record import AccessControlRecord
from openapi_server.models.access_control_record_list import AccessControlRecordList
from openapi_server.models.access_control_record_properties import AccessControlRecordProperties
from openapi_server.models.acs_configuration import AcsConfiguration
from openapi_server.models.alert import Alert
from openapi_server.models.alert_error_details import AlertErrorDetails
from openapi_server.models.alert_filter import AlertFilter
from openapi_server.models.alert_list import AlertList
from openapi_server.models.alert_notification_properties import AlertNotificationProperties
from openapi_server.models.alert_properties import AlertProperties
from openapi_server.models.alert_settings import AlertSettings
from openapi_server.models.alert_source import AlertSource
from openapi_server.models.asymmetric_encrypted_secret import AsymmetricEncryptedSecret
from openapi_server.models.available_provider_operation import AvailableProviderOperation
from openapi_server.models.available_provider_operation_display import AvailableProviderOperationDisplay
from openapi_server.models.available_provider_operation_list import AvailableProviderOperationList
from openapi_server.models.backup import Backup
from openapi_server.models.backup_element import BackupElement
from openapi_server.models.backup_filter import BackupFilter
from openapi_server.models.backup_list import BackupList
from openapi_server.models.backup_policy import BackupPolicy
from openapi_server.models.backup_policy_list import BackupPolicyList
from openapi_server.models.backup_policy_properties import BackupPolicyProperties
from openapi_server.models.backup_properties import BackupProperties
from openapi_server.models.backup_schedule import BackupSchedule
from openapi_server.models.backup_schedule_list import BackupScheduleList
from openapi_server.models.backup_schedule_properties import BackupScheduleProperties
from openapi_server.models.bandwidth_rate_setting_properties import BandwidthRateSettingProperties
from openapi_server.models.bandwidth_schedule import BandwidthSchedule
from openapi_server.models.bandwidth_setting import BandwidthSetting
from openapi_server.models.bandwidth_setting_list import BandwidthSettingList
from openapi_server.models.base_model import BaseModel
from openapi_server.models.chap_settings import ChapSettings
from openapi_server.models.clear_alert_request import ClearAlertRequest
from openapi_server.models.clone_request import CloneRequest
from openapi_server.models.cloud_appliance import CloudAppliance
from openapi_server.models.cloud_appliance_configuration import CloudApplianceConfiguration
from openapi_server.models.cloud_appliance_configuration_list import CloudApplianceConfigurationList
from openapi_server.models.cloud_appliance_configuration_properties import CloudApplianceConfigurationProperties
from openapi_server.models.cloud_appliance_settings import CloudApplianceSettings
from openapi_server.models.configure_device_request import ConfigureDeviceRequest
from openapi_server.models.configure_device_request_properties import ConfigureDeviceRequestProperties
from openapi_server.models.controller_power_state_change_request import ControllerPowerStateChangeRequest
from openapi_server.models.controller_power_state_change_request_properties import ControllerPowerStateChangeRequestProperties
from openapi_server.models.dns_settings import DNSSettings
from openapi_server.models.data_statistics import DataStatistics
from openapi_server.models.device import Device
from openapi_server.models.device_details import DeviceDetails
from openapi_server.models.device_list import DeviceList
from openapi_server.models.device_patch import DevicePatch
from openapi_server.models.device_patch_properties import DevicePatchProperties
from openapi_server.models.device_properties import DeviceProperties
from openapi_server.models.device_rollover_details import DeviceRolloverDetails
from openapi_server.models.dimension_filter import DimensionFilter
from openapi_server.models.encryption_settings import EncryptionSettings
from openapi_server.models.encryption_settings_properties import EncryptionSettingsProperties
from openapi_server.models.failover_request import FailoverRequest
from openapi_server.models.failover_set import FailoverSet
from openapi_server.models.failover_set_eligibility_result import FailoverSetEligibilityResult
from openapi_server.models.failover_sets_list import FailoverSetsList
from openapi_server.models.failover_target import FailoverTarget
from openapi_server.models.failover_targets_list import FailoverTargetsList
from openapi_server.models.feature import Feature
from openapi_server.models.feature_filter import FeatureFilter
from openapi_server.models.feature_list import FeatureList
from openapi_server.models.hardware_component import HardwareComponent
from openapi_server.models.hardware_component_group import HardwareComponentGroup
from openapi_server.models.hardware_component_group_list import HardwareComponentGroupList
from openapi_server.models.hardware_component_group_properties import HardwareComponentGroupProperties
from openapi_server.models.job import Job
from openapi_server.models.job_error_details import JobErrorDetails
from openapi_server.models.job_error_item import JobErrorItem
from openapi_server.models.job_filter import JobFilter
from openapi_server.models.job_list import JobList
from openapi_server.models.job_properties import JobProperties
from openapi_server.models.job_stage import JobStage
from openapi_server.models.key import Key
from openapi_server.models.list_failover_targets_request import ListFailoverTargetsRequest
from openapi_server.models.manager import Manager
from openapi_server.models.manager_extended_info import ManagerExtendedInfo
from openapi_server.models.manager_extended_info_properties import ManagerExtendedInfoProperties
from openapi_server.models.manager_intrinsic_settings import ManagerIntrinsicSettings
from openapi_server.models.manager_list import ManagerList
from openapi_server.models.manager_patch import ManagerPatch
from openapi_server.models.manager_properties import ManagerProperties
from openapi_server.models.manager_sku import ManagerSku
from openapi_server.models.metric_availablity import MetricAvailablity
from openapi_server.models.metric_data import MetricData
from openapi_server.models.metric_definition import MetricDefinition
from openapi_server.models.metric_definition_list import MetricDefinitionList
from openapi_server.models.metric_dimension import MetricDimension
from openapi_server.models.metric_filter import MetricFilter
from openapi_server.models.metric_list import MetricList
from openapi_server.models.metric_name import MetricName
from openapi_server.models.metric_name_filter import MetricNameFilter
from openapi_server.models.metrics import Metrics
from openapi_server.models.network_adapter_list import NetworkAdapterList
from openapi_server.models.network_adapters import NetworkAdapters
from openapi_server.models.network_interface_data0_settings import NetworkInterfaceData0Settings
from openapi_server.models.network_settings import NetworkSettings
from openapi_server.models.network_settings_patch import NetworkSettingsPatch
from openapi_server.models.network_settings_patch_properties import NetworkSettingsPatchProperties
from openapi_server.models.network_settings_properties import NetworkSettingsProperties
from openapi_server.models.nic_ipv4 import NicIPv4
from openapi_server.models.nic_ipv6 import NicIPv6
from openapi_server.models.public_key import PublicKey
from openapi_server.models.remote_management_settings import RemoteManagementSettings
from openapi_server.models.remote_management_settings_patch import RemoteManagementSettingsPatch
from openapi_server.models.resource import Resource
from openapi_server.models.schedule_recurrence import ScheduleRecurrence
from openapi_server.models.secondary_dns_settings import SecondaryDNSSettings
from openapi_server.models.security_settings import SecuritySettings
from openapi_server.models.security_settings_patch import SecuritySettingsPatch
from openapi_server.models.security_settings_patch_properties import SecuritySettingsPatchProperties
from openapi_server.models.security_settings_properties import SecuritySettingsProperties
from openapi_server.models.send_test_alert_email_request import SendTestAlertEmailRequest
from openapi_server.models.storage_account_credential import StorageAccountCredential
from openapi_server.models.storage_account_credential_list import StorageAccountCredentialList
from openapi_server.models.storage_account_credential_properties import StorageAccountCredentialProperties
from openapi_server.models.symmetric_encrypted_secret import SymmetricEncryptedSecret
from openapi_server.models.target_eligibility_error_message import TargetEligibilityErrorMessage
from openapi_server.models.target_eligibility_result import TargetEligibilityResult
from openapi_server.models.time import Time
from openapi_server.models.time_settings import TimeSettings
from openapi_server.models.time_settings_properties import TimeSettingsProperties
from openapi_server.models.updates import Updates
from openapi_server.models.updates_properties import UpdatesProperties
from openapi_server.models.vm_image import VmImage
from openapi_server.models.volume import Volume
from openapi_server.models.volume_container import VolumeContainer
from openapi_server.models.volume_container_failover_metadata import VolumeContainerFailoverMetadata
from openapi_server.models.volume_container_list import VolumeContainerList
from openapi_server.models.volume_container_properties import VolumeContainerProperties
from openapi_server.models.volume_failover_metadata import VolumeFailoverMetadata
from openapi_server.models.volume_list import VolumeList
from openapi_server.models.volume_properties import VolumeProperties
from openapi_server.models.webproxy_settings import WebproxySettings
