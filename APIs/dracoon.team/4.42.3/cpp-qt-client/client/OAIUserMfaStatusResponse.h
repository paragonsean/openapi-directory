/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUserMfaStatusResponse.h
 *
 * Contains information about the user&#39;s MFA status
 */

#ifndef OAIUserMfaStatusResponse_H
#define OAIUserMfaStatusResponse_H

#include <QJsonObject>

#include "OAIMfaSetupStatus.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIMfaSetupStatus;

class OAIUserMfaStatusResponse : public OAIObject {
public:
    OAIUserMfaStatusResponse();
    OAIUserMfaStatusResponse(QString json);
    ~OAIUserMfaStatusResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isMfaEnforced() const;
    void setMfaEnforced(const bool &mfa_enforced);
    bool is_mfa_enforced_Set() const;
    bool is_mfa_enforced_Valid() const;

    QList<OAIMfaSetupStatus> getMfaSetups() const;
    void setMfaSetups(const QList<OAIMfaSetupStatus> &mfa_setups);
    bool is_mfa_setups_Set() const;
    bool is_mfa_setups_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_mfa_enforced;
    bool m_mfa_enforced_isSet;
    bool m_mfa_enforced_isValid;

    QList<OAIMfaSetupStatus> m_mfa_setups;
    bool m_mfa_setups_isSet;
    bool m_mfa_setups_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUserMfaStatusResponse)

#endif // OAIUserMfaStatusResponse_H
