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
 * OAICreateOrganizationNetwork_request.h
 *
 * 
 */

#ifndef OAICreateOrganizationNetwork_request_H
#define OAICreateOrganizationNetwork_request_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICreateOrganizationNetwork_request : public OAIObject {
public:
    OAICreateOrganizationNetwork_request();
    OAICreateOrganizationNetwork_request(QString json);
    ~OAICreateOrganizationNetwork_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCopyFromNetworkId() const;
    void setCopyFromNetworkId(const QString &copy_from_network_id);
    bool is_copy_from_network_id_Set() const;
    bool is_copy_from_network_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getNotes() const;
    void setNotes(const QString &notes);
    bool is_notes_Set() const;
    bool is_notes_Valid() const;

    QList<QString> getProductTypes() const;
    void setProductTypes(const QList<QString> &product_types);
    bool is_product_types_Set() const;
    bool is_product_types_Valid() const;

    QList<QString> getTags() const;
    void setTags(const QList<QString> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    QString getTimeZone() const;
    void setTimeZone(const QString &time_zone);
    bool is_time_zone_Set() const;
    bool is_time_zone_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_copy_from_network_id;
    bool m_copy_from_network_id_isSet;
    bool m_copy_from_network_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_notes;
    bool m_notes_isSet;
    bool m_notes_isValid;

    QList<QString> m_product_types;
    bool m_product_types_isSet;
    bool m_product_types_isValid;

    QList<QString> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;

    QString m_time_zone;
    bool m_time_zone_isSet;
    bool m_time_zone_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateOrganizationNetwork_request)

#endif // OAICreateOrganizationNetwork_request_H
