/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICreateOrganizationAdaptivePolicyPolicy_request_sourceGroup.h
 *
 * The source adaptive policy group (requires one unique attribute)
 */

#ifndef OAICreateOrganizationAdaptivePolicyPolicy_request_sourceGroup_H
#define OAICreateOrganizationAdaptivePolicyPolicy_request_sourceGroup_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICreateOrganizationAdaptivePolicyPolicy_request_sourceGroup : public OAIObject {
public:
    OAICreateOrganizationAdaptivePolicyPolicy_request_sourceGroup();
    OAICreateOrganizationAdaptivePolicyPolicy_request_sourceGroup(QString json);
    ~OAICreateOrganizationAdaptivePolicyPolicy_request_sourceGroup() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getSgt() const;
    void setSgt(const qint32 &sgt);
    bool is_sgt_Set() const;
    bool is_sgt_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_sgt;
    bool m_sgt_isSet;
    bool m_sgt_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateOrganizationAdaptivePolicyPolicy_request_sourceGroup)

#endif // OAICreateOrganizationAdaptivePolicyPolicy_request_sourceGroup_H
