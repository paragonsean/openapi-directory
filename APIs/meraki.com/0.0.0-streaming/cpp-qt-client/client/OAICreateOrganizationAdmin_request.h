/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICreateOrganizationAdmin_request.h
 *
 * 
 */

#ifndef OAICreateOrganizationAdmin_request_H
#define OAICreateOrganizationAdmin_request_H

#include <QJsonObject>

#include "OAICreateOrganizationAdmin_request_networks_inner.h"
#include "OAICreateOrganizationAdmin_request_tags_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICreateOrganizationAdmin_request_networks_inner;
class OAICreateOrganizationAdmin_request_tags_inner;

class OAICreateOrganizationAdmin_request : public OAIObject {
public:
    OAICreateOrganizationAdmin_request();
    OAICreateOrganizationAdmin_request(QString json);
    ~OAICreateOrganizationAdmin_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAuthenticationMethod() const;
    void setAuthenticationMethod(const QString &authentication_method);
    bool is_authentication_method_Set() const;
    bool is_authentication_method_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<OAICreateOrganizationAdmin_request_networks_inner> getNetworks() const;
    void setNetworks(const QList<OAICreateOrganizationAdmin_request_networks_inner> &networks);
    bool is_networks_Set() const;
    bool is_networks_Valid() const;

    QString getOrgAccess() const;
    void setOrgAccess(const QString &org_access);
    bool is_org_access_Set() const;
    bool is_org_access_Valid() const;

    QList<OAICreateOrganizationAdmin_request_tags_inner> getTags() const;
    void setTags(const QList<OAICreateOrganizationAdmin_request_tags_inner> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_authentication_method;
    bool m_authentication_method_isSet;
    bool m_authentication_method_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<OAICreateOrganizationAdmin_request_networks_inner> m_networks;
    bool m_networks_isSet;
    bool m_networks_isValid;

    QString m_org_access;
    bool m_org_access_isSet;
    bool m_org_access_isValid;

    QList<OAICreateOrganizationAdmin_request_tags_inner> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateOrganizationAdmin_request)

#endif // OAICreateOrganizationAdmin_request_H
