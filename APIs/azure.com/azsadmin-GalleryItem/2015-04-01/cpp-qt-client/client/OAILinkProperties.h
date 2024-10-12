/**
 * GalleryManagementClient
 * The Admin Gallery Management Client.
 *
 * The version of the OpenAPI document: 2015-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAILinkProperties.h
 *
 * Represents a link item read from the gallery item package.
 */

#ifndef OAILinkProperties_H
#define OAILinkProperties_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAILinkProperties : public OAIObject {
public:
    OAILinkProperties();
    OAILinkProperties(QString json);
    ~OAILinkProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDisplayName() const;
    void setDisplayName(const QString &display_name);
    bool is_display_name_Set() const;
    bool is_display_name_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getUri() const;
    void setUri(const QString &uri);
    bool is_uri_Set() const;
    bool is_uri_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_display_name;
    bool m_display_name_isSet;
    bool m_display_name_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_uri;
    bool m_uri_isSet;
    bool m_uri_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILinkProperties)

#endif // OAILinkProperties_H
