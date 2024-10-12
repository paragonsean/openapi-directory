/**
 * ConfigCat Public Management API
 * **Base API URL**: https://api.configcat.com  If you prefer the swagger documentation, you can find it here: [Swagger UI](https://api.configcat.com/swagger).  The purpose of this API is to access the ConfigCat platform programmatically.  You can **Create**, **Read**, **Update** and **Delete** any entities like **Feature Flags, Configs, Environments** or **Products** within ConfigCat.   The API is based on HTTP REST, uses resource-oriented URLs, status codes and supports JSON  and JSON+HAL format. Do not use this API for accessing and evaluating feature flag values. Use the [SDKs instead](https://configcat.com/docs/sdk-reference/overview).   # OpenAPI Specification  The complete specification is publicly available here: [swagger.json](v1/swagger.json).  You can use it to generate client libraries in various languages with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) or [Swagger Codegen](https://swagger.io/tools/swagger-codegen/) to interact with this API.  # Authentication This API uses the [Basic HTTP Authentication Scheme](https://en.wikipedia.org/wiki/Basic_access_authentication).   <!-- ReDoc-Inject: <security-definitions> -->  # Throttling and rate limits All the rate limited API calls are returning information about the current rate limit period in the following HTTP headers:  | Header | Description | | :- | :- | | X-Rate-Limit-Remaining | The maximum number of requests remaining in the current rate limit period. | | X-Rate-Limit-Reset     | The time when the current rate limit period resets.        |  When the rate limit is exceeded by a request, the API returns with a `HTTP 429 - Too many requests` status along with a `Retry-After` HTTP header. 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@configcat.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAuditLogType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAuditLogType::OAIAuditLogType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAuditLogType::OAIAuditLogType() {
    this->initializeModel();
}

OAIAuditLogType::~OAIAuditLogType() {}

void OAIAuditLogType::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIAuditLogType::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIAuditLogType::fromJson(QString jsonString) {
    
    if ( jsonString.compare("productCreated", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::PRODUCTCREATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("productChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::PRODUCTCHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("productOwnershipTransferred", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::PRODUCTOWNERSHIPTRANSFERRED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("productDeleted", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::PRODUCTDELETED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("productsReordered", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::PRODUCTSREORDERED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("teamMemberInvited", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::TEAMMEMBERINVITED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("teamMemberInvitationRevoked", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::TEAMMEMBERINVITATIONREVOKED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("teamMemberJoined", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::TEAMMEMBERJOINED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("teamMemberPermissionGroupChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::TEAMMEMBERPERMISSIONGROUPCHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("teamMemberRemoved", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::TEAMMEMBERREMOVED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("teamMemberLeft", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::TEAMMEMBERLEFT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("teamMemberInvitationChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::TEAMMEMBERINVITATIONCHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("teamMemberInvitationResent", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::TEAMMEMBERINVITATIONRESENT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("teamMemberInvitationRejected", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::TEAMMEMBERINVITATIONREJECTED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("configCreated", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::CONFIGCREATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("configChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::CONFIGCHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("configDeleted", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::CONFIGDELETED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("configsReordered", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::CONFIGSREORDERED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("environmentCreated", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::ENVIRONMENTCREATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("environmentChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::ENVIRONMENTCHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("environmentDeleted", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::ENVIRONMENTDELETED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("environmentsReordered", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::ENVIRONMENTSREORDERED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("settingCreated", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::SETTINGCREATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("settingChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::SETTINGCHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("settingDeleted", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::SETTINGDELETED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("settingsReordered", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::SETTINGSREORDERED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("settingValueChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::SETTINGVALUECHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("webHookCreated", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::WEBHOOKCREATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("webHookChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::WEBHOOKCHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("webHookDeleted", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::WEBHOOKDELETED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("subscriptionChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::SUBSCRIPTIONCHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("permissionGroupCreated", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::PERMISSIONGROUPCREATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("permissionGroupChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::PERMISSIONGROUPCHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("permissionGroupDeleted", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::PERMISSIONGROUPDELETED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("permissionGroupDefault", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::PERMISSIONGROUPDEFAULT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("apiKeyAdded", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::APIKEYADDED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("apiKeyRemoved", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::APIKEYREMOVED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("integrationAdded", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::INTEGRATIONADDED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("integrationChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::INTEGRATIONCHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("integrationRemoved", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::INTEGRATIONREMOVED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("apiKeyConnected", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::APIKEYCONNECTED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("integrationLinkAdded", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::INTEGRATIONLINKADDED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("integrationLinkRemoved", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::INTEGRATIONLINKREMOVED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("organizationAdded", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::ORGANIZATIONADDED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("organizationRemoved", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::ORGANIZATIONREMOVED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("organizationChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::ORGANIZATIONCHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("organizationSubscriptionTypeChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::ORGANIZATIONSUBSCRIPTIONTYPECHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("organizationAdminChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::ORGANIZATIONADMINCHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("organizationAdminLeft", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::ORGANIZATIONADMINLEFT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("organizationAdminDisabled2FA", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::ORGANIZATIONADMINDISABLED2FA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("tagAdded", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::TAGADDED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("tagChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::TAGCHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("tagRemoved", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::TAGREMOVED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("settingTagAdded", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::SETTINGTAGADDED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("settingTagRemoved", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::SETTINGTAGREMOVED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("publicApiAccessTokenAdded", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::PUBLICAPIACCESSTOKENADDED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("publicApiAccessTokenRemoved", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::PUBLICAPIACCESSTOKENREMOVED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("domainAdded", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::DOMAINADDED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("domainVerified", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::DOMAINVERIFIED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("domainRemoved", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::DOMAINREMOVED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("domainSamlConfigured", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::DOMAINSAMLCONFIGURED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("domainSamlDeleted", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::DOMAINSAMLDELETED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("autoProvisioningConfigurationChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::AUTOPROVISIONINGCONFIGURATIONCHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("organizationMemberJoined", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::ORGANIZATIONMEMBERJOINED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("organizationMemberProductJoinRequested", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::ORGANIZATIONMEMBERPRODUCTJOINREQUESTED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("organizationMemberProductJoinRequestRejected", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::ORGANIZATIONMEMBERPRODUCTJOINREQUESTREJECTED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("organizationMemberProductJoinRequestApproved", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::ORGANIZATIONMEMBERPRODUCTJOINREQUESTAPPROVED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("codeReferencesUploaded", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::CODEREFERENCESUPLOADED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("codeReferenceDeleted", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::CODEREFERENCEDELETED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("codeReferenceStaleBranchDeleted", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::CODEREFERENCESTALEBRANCHDELETED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("segmentCreated", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::SEGMENTCREATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("segmentChanged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::SEGMENTCHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("segmentDeleted", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::SEGMENTDELETED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("webhookSigningKeyDeleted", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::WEBHOOKSIGNINGKEYDELETED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("webhookSigningKeyCreated", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAuditLogType::WEBHOOKSIGNINGKEYCREATED;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIAuditLogType::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIAuditLogType::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIAuditLogType::PRODUCTCREATED:
            val = "productCreated";
            break;
        case eOAIAuditLogType::PRODUCTCHANGED:
            val = "productChanged";
            break;
        case eOAIAuditLogType::PRODUCTOWNERSHIPTRANSFERRED:
            val = "productOwnershipTransferred";
            break;
        case eOAIAuditLogType::PRODUCTDELETED:
            val = "productDeleted";
            break;
        case eOAIAuditLogType::PRODUCTSREORDERED:
            val = "productsReordered";
            break;
        case eOAIAuditLogType::TEAMMEMBERINVITED:
            val = "teamMemberInvited";
            break;
        case eOAIAuditLogType::TEAMMEMBERINVITATIONREVOKED:
            val = "teamMemberInvitationRevoked";
            break;
        case eOAIAuditLogType::TEAMMEMBERJOINED:
            val = "teamMemberJoined";
            break;
        case eOAIAuditLogType::TEAMMEMBERPERMISSIONGROUPCHANGED:
            val = "teamMemberPermissionGroupChanged";
            break;
        case eOAIAuditLogType::TEAMMEMBERREMOVED:
            val = "teamMemberRemoved";
            break;
        case eOAIAuditLogType::TEAMMEMBERLEFT:
            val = "teamMemberLeft";
            break;
        case eOAIAuditLogType::TEAMMEMBERINVITATIONCHANGED:
            val = "teamMemberInvitationChanged";
            break;
        case eOAIAuditLogType::TEAMMEMBERINVITATIONRESENT:
            val = "teamMemberInvitationResent";
            break;
        case eOAIAuditLogType::TEAMMEMBERINVITATIONREJECTED:
            val = "teamMemberInvitationRejected";
            break;
        case eOAIAuditLogType::CONFIGCREATED:
            val = "configCreated";
            break;
        case eOAIAuditLogType::CONFIGCHANGED:
            val = "configChanged";
            break;
        case eOAIAuditLogType::CONFIGDELETED:
            val = "configDeleted";
            break;
        case eOAIAuditLogType::CONFIGSREORDERED:
            val = "configsReordered";
            break;
        case eOAIAuditLogType::ENVIRONMENTCREATED:
            val = "environmentCreated";
            break;
        case eOAIAuditLogType::ENVIRONMENTCHANGED:
            val = "environmentChanged";
            break;
        case eOAIAuditLogType::ENVIRONMENTDELETED:
            val = "environmentDeleted";
            break;
        case eOAIAuditLogType::ENVIRONMENTSREORDERED:
            val = "environmentsReordered";
            break;
        case eOAIAuditLogType::SETTINGCREATED:
            val = "settingCreated";
            break;
        case eOAIAuditLogType::SETTINGCHANGED:
            val = "settingChanged";
            break;
        case eOAIAuditLogType::SETTINGDELETED:
            val = "settingDeleted";
            break;
        case eOAIAuditLogType::SETTINGSREORDERED:
            val = "settingsReordered";
            break;
        case eOAIAuditLogType::SETTINGVALUECHANGED:
            val = "settingValueChanged";
            break;
        case eOAIAuditLogType::WEBHOOKCREATED:
            val = "webHookCreated";
            break;
        case eOAIAuditLogType::WEBHOOKCHANGED:
            val = "webHookChanged";
            break;
        case eOAIAuditLogType::WEBHOOKDELETED:
            val = "webHookDeleted";
            break;
        case eOAIAuditLogType::SUBSCRIPTIONCHANGED:
            val = "subscriptionChanged";
            break;
        case eOAIAuditLogType::PERMISSIONGROUPCREATED:
            val = "permissionGroupCreated";
            break;
        case eOAIAuditLogType::PERMISSIONGROUPCHANGED:
            val = "permissionGroupChanged";
            break;
        case eOAIAuditLogType::PERMISSIONGROUPDELETED:
            val = "permissionGroupDeleted";
            break;
        case eOAIAuditLogType::PERMISSIONGROUPDEFAULT:
            val = "permissionGroupDefault";
            break;
        case eOAIAuditLogType::APIKEYADDED:
            val = "apiKeyAdded";
            break;
        case eOAIAuditLogType::APIKEYREMOVED:
            val = "apiKeyRemoved";
            break;
        case eOAIAuditLogType::INTEGRATIONADDED:
            val = "integrationAdded";
            break;
        case eOAIAuditLogType::INTEGRATIONCHANGED:
            val = "integrationChanged";
            break;
        case eOAIAuditLogType::INTEGRATIONREMOVED:
            val = "integrationRemoved";
            break;
        case eOAIAuditLogType::APIKEYCONNECTED:
            val = "apiKeyConnected";
            break;
        case eOAIAuditLogType::INTEGRATIONLINKADDED:
            val = "integrationLinkAdded";
            break;
        case eOAIAuditLogType::INTEGRATIONLINKREMOVED:
            val = "integrationLinkRemoved";
            break;
        case eOAIAuditLogType::ORGANIZATIONADDED:
            val = "organizationAdded";
            break;
        case eOAIAuditLogType::ORGANIZATIONREMOVED:
            val = "organizationRemoved";
            break;
        case eOAIAuditLogType::ORGANIZATIONCHANGED:
            val = "organizationChanged";
            break;
        case eOAIAuditLogType::ORGANIZATIONSUBSCRIPTIONTYPECHANGED:
            val = "organizationSubscriptionTypeChanged";
            break;
        case eOAIAuditLogType::ORGANIZATIONADMINCHANGED:
            val = "organizationAdminChanged";
            break;
        case eOAIAuditLogType::ORGANIZATIONADMINLEFT:
            val = "organizationAdminLeft";
            break;
        case eOAIAuditLogType::ORGANIZATIONADMINDISABLED2FA:
            val = "organizationAdminDisabled2FA";
            break;
        case eOAIAuditLogType::TAGADDED:
            val = "tagAdded";
            break;
        case eOAIAuditLogType::TAGCHANGED:
            val = "tagChanged";
            break;
        case eOAIAuditLogType::TAGREMOVED:
            val = "tagRemoved";
            break;
        case eOAIAuditLogType::SETTINGTAGADDED:
            val = "settingTagAdded";
            break;
        case eOAIAuditLogType::SETTINGTAGREMOVED:
            val = "settingTagRemoved";
            break;
        case eOAIAuditLogType::PUBLICAPIACCESSTOKENADDED:
            val = "publicApiAccessTokenAdded";
            break;
        case eOAIAuditLogType::PUBLICAPIACCESSTOKENREMOVED:
            val = "publicApiAccessTokenRemoved";
            break;
        case eOAIAuditLogType::DOMAINADDED:
            val = "domainAdded";
            break;
        case eOAIAuditLogType::DOMAINVERIFIED:
            val = "domainVerified";
            break;
        case eOAIAuditLogType::DOMAINREMOVED:
            val = "domainRemoved";
            break;
        case eOAIAuditLogType::DOMAINSAMLCONFIGURED:
            val = "domainSamlConfigured";
            break;
        case eOAIAuditLogType::DOMAINSAMLDELETED:
            val = "domainSamlDeleted";
            break;
        case eOAIAuditLogType::AUTOPROVISIONINGCONFIGURATIONCHANGED:
            val = "autoProvisioningConfigurationChanged";
            break;
        case eOAIAuditLogType::ORGANIZATIONMEMBERJOINED:
            val = "organizationMemberJoined";
            break;
        case eOAIAuditLogType::ORGANIZATIONMEMBERPRODUCTJOINREQUESTED:
            val = "organizationMemberProductJoinRequested";
            break;
        case eOAIAuditLogType::ORGANIZATIONMEMBERPRODUCTJOINREQUESTREJECTED:
            val = "organizationMemberProductJoinRequestRejected";
            break;
        case eOAIAuditLogType::ORGANIZATIONMEMBERPRODUCTJOINREQUESTAPPROVED:
            val = "organizationMemberProductJoinRequestApproved";
            break;
        case eOAIAuditLogType::CODEREFERENCESUPLOADED:
            val = "codeReferencesUploaded";
            break;
        case eOAIAuditLogType::CODEREFERENCEDELETED:
            val = "codeReferenceDeleted";
            break;
        case eOAIAuditLogType::CODEREFERENCESTALEBRANCHDELETED:
            val = "codeReferenceStaleBranchDeleted";
            break;
        case eOAIAuditLogType::SEGMENTCREATED:
            val = "segmentCreated";
            break;
        case eOAIAuditLogType::SEGMENTCHANGED:
            val = "segmentChanged";
            break;
        case eOAIAuditLogType::SEGMENTDELETED:
            val = "segmentDeleted";
            break;
        case eOAIAuditLogType::WEBHOOKSIGNINGKEYDELETED:
            val = "webhookSigningKeyDeleted";
            break;
        case eOAIAuditLogType::WEBHOOKSIGNINGKEYCREATED:
            val = "webhookSigningKeyCreated";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIAuditLogType::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIAuditLogType::eOAIAuditLogType OAIAuditLogType::getValue() const {
    return m_value;
}

void OAIAuditLogType::setValue(const OAIAuditLogType::eOAIAuditLogType& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIAuditLogType::isSet() const {
    
    return m_value_isSet;
}

bool OAIAuditLogType::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
