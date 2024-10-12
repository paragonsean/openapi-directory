# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_apps_drive_labels_v2_batch_delete_label_permissions_request import GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequest
from openapi_server.models.google_apps_drive_labels_v2_batch_update_label_permissions_request import GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequest
from openapi_server.models.google_apps_drive_labels_v2_batch_update_label_permissions_response import GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponse
from openapi_server.models.google_apps_drive_labels_v2_delta_update_label_request import GoogleAppsDriveLabelsV2DeltaUpdateLabelRequest
from openapi_server.models.google_apps_drive_labels_v2_delta_update_label_response import GoogleAppsDriveLabelsV2DeltaUpdateLabelResponse
from openapi_server.models.google_apps_drive_labels_v2_disable_label_request import GoogleAppsDriveLabelsV2DisableLabelRequest
from openapi_server.models.google_apps_drive_labels_v2_enable_label_request import GoogleAppsDriveLabelsV2EnableLabelRequest
from openapi_server.models.google_apps_drive_labels_v2_label import GoogleAppsDriveLabelsV2Label
from openapi_server.models.google_apps_drive_labels_v2_label_permission import GoogleAppsDriveLabelsV2LabelPermission
from openapi_server.models.google_apps_drive_labels_v2_list_label_locks_response import GoogleAppsDriveLabelsV2ListLabelLocksResponse
from openapi_server.models.google_apps_drive_labels_v2_list_label_permissions_response import GoogleAppsDriveLabelsV2ListLabelPermissionsResponse
from openapi_server.models.google_apps_drive_labels_v2_list_labels_response import GoogleAppsDriveLabelsV2ListLabelsResponse
from openapi_server.models.google_apps_drive_labels_v2_publish_label_request import GoogleAppsDriveLabelsV2PublishLabelRequest
from openapi_server.models.google_apps_drive_labels_v2_update_label_copy_mode_request import GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequest


pytestmark = pytest.mark.asyncio

async def test_drivelabels_labels_create(client):
    """Test case for drivelabels_labels_create

    
    """
    body = {"publishTime":"publishTime","creator":{"person":"person"},"labelType":"LABEL_TYPE_UNSPECIFIED","learnMoreUri":"learnMoreUri","revisionCreateTime":"revisionCreateTime","disabler":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"revisionId":"revisionId","appliedLabelPolicy":{"copyMode":"COPY_MODE_UNSPECIFIED"},"displayHints":{"hiddenInSearch":True,"disabled":True,"shownInApply":True,"priority":"priority"},"lockStatus":{"locked":True},"createTime":"createTime","revisionCreator":{"person":"person"},"schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"name":"name","appliedCapabilities":{"canApply":True,"canRemove":True,"canRead":True},"publisher":{"person":"person"},"id":"id","fields":[{"creator":{"person":"person"},"queryKey":"queryKey","textOptions":{"minLength":2,"maxLength":3},"selectionOptions":{"listOptions":{"maxEntries":9},"choices":[{"publishTime":"publishTime","creator":{"person":"person"},"updateTime":"updateTime","disabler":{"person":"person"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"displayHints":{"darkBadgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}},"hiddenInSearch":True,"badgePriority":"badgePriority","disabled":True,"shownInApply":True,"badgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}}},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canSelect":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"disableTime":"disableTime"},{"publishTime":"publishTime","creator":{"person":"person"},"updateTime":"updateTime","disabler":{"person":"person"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"displayHints":{"darkBadgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}},"hiddenInSearch":True,"badgePriority":"badgePriority","disabled":True,"shownInApply":True,"badgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}}},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canSelect":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"disableTime":"disableTime"}]},"updateTime":"updateTime","disabler":{"person":"person"},"integerOptions":{"minValue":"minValue","maxValue":"maxValue"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"dateOptions":{"minValue":{"month":6,"year":1,"day":0},"dateFormat":"dateFormat","maxValue":{"month":6,"year":1,"day":0},"dateFormatType":"DATE_FORMAT_UNSPECIFIED"},"displayHints":{"hiddenInSearch":True,"disabled":True,"shownInApply":True,"required":True},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canWrite":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","userOptions":{"listOptions":{"maxEntries":9}},"properties":{"displayName":"displayName","insertBeforeField":"insertBeforeField","required":True},"disableTime":"disableTime"},{"creator":{"person":"person"},"queryKey":"queryKey","textOptions":{"minLength":2,"maxLength":3},"selectionOptions":{"listOptions":{"maxEntries":9},"choices":[{"publishTime":"publishTime","creator":{"person":"person"},"updateTime":"updateTime","disabler":{"person":"person"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"displayHints":{"darkBadgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}},"hiddenInSearch":True,"badgePriority":"badgePriority","disabled":True,"shownInApply":True,"badgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}}},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canSelect":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"disableTime":"disableTime"},{"publishTime":"publishTime","creator":{"person":"person"},"updateTime":"updateTime","disabler":{"person":"person"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"displayHints":{"darkBadgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}},"hiddenInSearch":True,"badgePriority":"badgePriority","disabled":True,"shownInApply":True,"badgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}}},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canSelect":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"disableTime":"disableTime"}]},"updateTime":"updateTime","disabler":{"person":"person"},"integerOptions":{"minValue":"minValue","maxValue":"maxValue"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"dateOptions":{"minValue":{"month":6,"year":1,"day":0},"dateFormat":"dateFormat","maxValue":{"month":6,"year":1,"day":0},"dateFormatType":"DATE_FORMAT_UNSPECIFIED"},"displayHints":{"hiddenInSearch":True,"disabled":True,"shownInApply":True,"required":True},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canWrite":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","userOptions":{"listOptions":{"maxEntries":9}},"properties":{"displayName":"displayName","insertBeforeField":"insertBeforeField","required":True},"disableTime":"disableTime"}],"properties":{"description":"description","title":"title"},"customer":"customer","disableTime":"disableTime"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('languageCode', 'language_code_example'),
                    ('useAdminAccess', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/labels',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivelabels_labels_delta(client):
    """Test case for drivelabels_labels_delta

    
    """
    body = {"view":"LABEL_VIEW_BASIC","useAdminAccess":True,"requests":[{"createField":{"field":{"creator":{"person":"person"},"queryKey":"queryKey","textOptions":{"minLength":2,"maxLength":3},"selectionOptions":{"listOptions":{"maxEntries":9},"choices":[{"publishTime":"publishTime","creator":{"person":"person"},"updateTime":"updateTime","disabler":{"person":"person"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"displayHints":{"darkBadgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}},"hiddenInSearch":True,"badgePriority":"badgePriority","disabled":True,"shownInApply":True,"badgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}}},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canSelect":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"disableTime":"disableTime"},{"publishTime":"publishTime","creator":{"person":"person"},"updateTime":"updateTime","disabler":{"person":"person"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"displayHints":{"darkBadgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}},"hiddenInSearch":True,"badgePriority":"badgePriority","disabled":True,"shownInApply":True,"badgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}}},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canSelect":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"disableTime":"disableTime"}]},"updateTime":"updateTime","disabler":{"person":"person"},"integerOptions":{"minValue":"minValue","maxValue":"maxValue"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"dateOptions":{"minValue":{"month":6,"year":1,"day":0},"dateFormat":"dateFormat","maxValue":{"month":6,"year":1,"day":0},"dateFormatType":"DATE_FORMAT_UNSPECIFIED"},"displayHints":{"hiddenInSearch":True,"disabled":True,"shownInApply":True,"required":True},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canWrite":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","userOptions":{"listOptions":{"maxEntries":9}},"properties":{"displayName":"displayName","insertBeforeField":"insertBeforeField","required":True},"disableTime":"disableTime"}},"disableSelectionChoice":{"disabledPolicy":{"showInApply":True,"hideInSearch":True},"id":"id","updateMask":"updateMask","fieldId":"fieldId"},"deleteField":{"id":"id"},"disableField":{"disabledPolicy":{"showInApply":True,"hideInSearch":True},"id":"id","updateMask":"updateMask"},"updateLabel":{"updateMask":"updateMask","properties":{"description":"description","title":"title"}},"enableField":{"id":"id"},"enableSelectionChoice":{"id":"id","fieldId":"fieldId"},"createSelectionChoice":{"choice":{"publishTime":"publishTime","creator":{"person":"person"},"updateTime":"updateTime","disabler":{"person":"person"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"displayHints":{"darkBadgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}},"hiddenInSearch":True,"badgePriority":"badgePriority","disabled":True,"shownInApply":True,"badgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}}},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canSelect":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"disableTime":"disableTime"},"fieldId":"fieldId"},"deleteSelectionChoice":{"id":"id","fieldId":"fieldId"},"updateField":{"id":"id","updateMask":"updateMask","properties":{"displayName":"displayName","insertBeforeField":"insertBeforeField","required":True}},"updateFieldType":{"dateOptions":{"minValue":{"month":6,"year":1,"day":0},"dateFormat":"dateFormat","maxValue":{"month":6,"year":1,"day":0},"dateFormatType":"DATE_FORMAT_UNSPECIFIED"},"textOptions":{"minLength":2,"maxLength":3},"selectionOptions":{"listOptions":{"maxEntries":9},"choices":[{"publishTime":"publishTime","creator":{"person":"person"},"updateTime":"updateTime","disabler":{"person":"person"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"displayHints":{"darkBadgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}},"hiddenInSearch":True,"badgePriority":"badgePriority","disabled":True,"shownInApply":True,"badgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}}},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canSelect":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"disableTime":"disableTime"},{"publishTime":"publishTime","creator":{"person":"person"},"updateTime":"updateTime","disabler":{"person":"person"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"displayHints":{"darkBadgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}},"hiddenInSearch":True,"badgePriority":"badgePriority","disabled":True,"shownInApply":True,"badgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}}},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canSelect":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"disableTime":"disableTime"}]},"id":"id","userOptions":{"listOptions":{"maxEntries":9}},"updateMask":"updateMask","integerOptions":{"minValue":"minValue","maxValue":"maxValue"}},"updateSelectionChoiceProperties":{"id":"id","updateMask":"updateMask","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"fieldId":"fieldId"}},{"createField":{"field":{"creator":{"person":"person"},"queryKey":"queryKey","textOptions":{"minLength":2,"maxLength":3},"selectionOptions":{"listOptions":{"maxEntries":9},"choices":[{"publishTime":"publishTime","creator":{"person":"person"},"updateTime":"updateTime","disabler":{"person":"person"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"displayHints":{"darkBadgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}},"hiddenInSearch":True,"badgePriority":"badgePriority","disabled":True,"shownInApply":True,"badgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}}},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canSelect":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"disableTime":"disableTime"},{"publishTime":"publishTime","creator":{"person":"person"},"updateTime":"updateTime","disabler":{"person":"person"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"displayHints":{"darkBadgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}},"hiddenInSearch":True,"badgePriority":"badgePriority","disabled":True,"shownInApply":True,"badgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}}},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canSelect":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"disableTime":"disableTime"}]},"updateTime":"updateTime","disabler":{"person":"person"},"integerOptions":{"minValue":"minValue","maxValue":"maxValue"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"dateOptions":{"minValue":{"month":6,"year":1,"day":0},"dateFormat":"dateFormat","maxValue":{"month":6,"year":1,"day":0},"dateFormatType":"DATE_FORMAT_UNSPECIFIED"},"displayHints":{"hiddenInSearch":True,"disabled":True,"shownInApply":True,"required":True},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canWrite":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","userOptions":{"listOptions":{"maxEntries":9}},"properties":{"displayName":"displayName","insertBeforeField":"insertBeforeField","required":True},"disableTime":"disableTime"}},"disableSelectionChoice":{"disabledPolicy":{"showInApply":True,"hideInSearch":True},"id":"id","updateMask":"updateMask","fieldId":"fieldId"},"deleteField":{"id":"id"},"disableField":{"disabledPolicy":{"showInApply":True,"hideInSearch":True},"id":"id","updateMask":"updateMask"},"updateLabel":{"updateMask":"updateMask","properties":{"description":"description","title":"title"}},"enableField":{"id":"id"},"enableSelectionChoice":{"id":"id","fieldId":"fieldId"},"createSelectionChoice":{"choice":{"publishTime":"publishTime","creator":{"person":"person"},"updateTime":"updateTime","disabler":{"person":"person"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"displayHints":{"darkBadgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}},"hiddenInSearch":True,"badgePriority":"badgePriority","disabled":True,"shownInApply":True,"badgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}}},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canSelect":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"disableTime":"disableTime"},"fieldId":"fieldId"},"deleteSelectionChoice":{"id":"id","fieldId":"fieldId"},"updateField":{"id":"id","updateMask":"updateMask","properties":{"displayName":"displayName","insertBeforeField":"insertBeforeField","required":True}},"updateFieldType":{"dateOptions":{"minValue":{"month":6,"year":1,"day":0},"dateFormat":"dateFormat","maxValue":{"month":6,"year":1,"day":0},"dateFormatType":"DATE_FORMAT_UNSPECIFIED"},"textOptions":{"minLength":2,"maxLength":3},"selectionOptions":{"listOptions":{"maxEntries":9},"choices":[{"publishTime":"publishTime","creator":{"person":"person"},"updateTime":"updateTime","disabler":{"person":"person"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"displayHints":{"darkBadgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}},"hiddenInSearch":True,"badgePriority":"badgePriority","disabled":True,"shownInApply":True,"badgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}}},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canSelect":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"disableTime":"disableTime"},{"publishTime":"publishTime","creator":{"person":"person"},"updateTime":"updateTime","disabler":{"person":"person"},"updater":{"person":"person"},"lifecycle":{"hasUnpublishedChanges":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"state":"STATE_UNSPECIFIED"},"displayHints":{"darkBadgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}},"hiddenInSearch":True,"badgePriority":"badgePriority","disabled":True,"shownInApply":True,"badgeColors":{"backgroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"foregroundColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"soloColor":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134}}},"lockStatus":{"locked":True},"createTime":"createTime","schemaCapabilities":{"canUpdate":True,"canEnable":True,"canDisable":True,"canDelete":True},"appliedCapabilities":{"canRead":True,"canSelect":True,"canSearch":True},"publisher":{"person":"person"},"id":"id","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"disableTime":"disableTime"}]},"id":"id","userOptions":{"listOptions":{"maxEntries":9}},"updateMask":"updateMask","integerOptions":{"minValue":"minValue","maxValue":"maxValue"}},"updateSelectionChoiceProperties":{"id":"id","updateMask":"updateMask","properties":{"displayName":"displayName","insertBeforeChoice":"insertBeforeChoice","description":"description","badgeConfig":{"color":{"red":7.0614014,"green":2.302136,"blue":5.637377,"alpha":5.962134},"priorityOverride":"priorityOverride"}},"fieldId":"fieldId"}}],"languageCode":"languageCode","writeControl":{"requiredRevisionId":"requiredRevisionId"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{namedelt}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivelabels_labels_disable(client):
    """Test case for drivelabels_labels_disable

    
    """
    body = {"useAdminAccess":True,"disabledPolicy":{"showInApply":True,"hideInSearch":True},"languageCode":"languageCode","updateMask":"updateMask","writeControl":{"requiredRevisionId":"requiredRevisionId"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{namedisabl}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivelabels_labels_enable(client):
    """Test case for drivelabels_labels_enable

    
    """
    body = {"useAdminAccess":True,"languageCode":"languageCode","writeControl":{"requiredRevisionId":"requiredRevisionId"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{nameenabl}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivelabels_labels_list(client):
    """Test case for drivelabels_labels_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('customer', 'customer_example'),
                    ('languageCode', 'language_code_example'),
                    ('minimumRole', 'minimum_role_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('publishedOnly', True),
                    ('useAdminAccess', True),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/labels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivelabels_labels_publish(client):
    """Test case for drivelabels_labels_publish

    
    """
    body = {"useAdminAccess":True,"languageCode":"languageCode","writeControl":{"requiredRevisionId":"requiredRevisionId"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{namepublis}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivelabels_labels_revisions_locks_list(client):
    """Test case for drivelabels_labels_revisions_locks_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/{parent}/locks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivelabels_labels_revisions_permissions_batch_delete(client):
    """Test case for drivelabels_labels_revisions_permissions_batch_delete

    
    """
    body = {"useAdminAccess":True,"requests":[{"useAdminAccess":True,"name":"name"},{"useAdminAccess":True,"name":"name"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{parent}/permissions:batchDelete'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivelabels_labels_revisions_permissions_batch_update(client):
    """Test case for drivelabels_labels_revisions_permissions_batch_update

    
    """
    body = {"useAdminAccess":True,"requests":[{"parent":"parent","useAdminAccess":True,"labelPermission":{"audience":"audience","role":"LABEL_ROLE_UNSPECIFIED","person":"person","name":"name","email":"email","group":"group"}},{"parent":"parent","useAdminAccess":True,"labelPermission":{"audience":"audience","role":"LABEL_ROLE_UNSPECIFIED","person":"person","name":"name","email":"email","group":"group"}}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{parent}/permissions:batchUpdate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivelabels_labels_revisions_permissions_create(client):
    """Test case for drivelabels_labels_revisions_permissions_create

    
    """
    body = {"audience":"audience","role":"LABEL_ROLE_UNSPECIFIED","person":"person","name":"name","email":"email","group":"group"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('useAdminAccess', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{parent}/permissions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivelabels_labels_revisions_permissions_delete(client):
    """Test case for drivelabels_labels_revisions_permissions_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('useAdminAccess', True),
                    ('writeControl.requiredRevisionId', 'write_control_required_revision_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivelabels_labels_revisions_permissions_list(client):
    """Test case for drivelabels_labels_revisions_permissions_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('useAdminAccess', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/{parent}/permissions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivelabels_labels_revisions_update_permissions(client):
    """Test case for drivelabels_labels_revisions_update_permissions

    
    """
    body = {"audience":"audience","role":"LABEL_ROLE_UNSPECIFIED","person":"person","name":"name","email":"email","group":"group"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('useAdminAccess', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/{parent}/permissions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drivelabels_labels_update_label_copy_mode(client):
    """Test case for drivelabels_labels_update_label_copy_mode

    
    """
    body = {"view":"LABEL_VIEW_BASIC","useAdminAccess":True,"copyMode":"COPY_MODE_UNSPECIFIED","languageCode":"languageCode"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{nameupdate_label_copy_mod}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

