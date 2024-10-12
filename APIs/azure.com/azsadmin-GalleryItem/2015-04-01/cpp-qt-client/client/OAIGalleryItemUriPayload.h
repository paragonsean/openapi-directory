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
 * OAIGalleryItemUriPayload.h
 *
 * Location of gallery item payload.
 */

#ifndef OAIGalleryItemUriPayload_H
#define OAIGalleryItemUriPayload_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGalleryItemUriPayload : public OAIObject {
public:
    OAIGalleryItemUriPayload();
    OAIGalleryItemUriPayload(QString json);
    ~OAIGalleryItemUriPayload() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getGalleryItemUri() const;
    void setGalleryItemUri(const QString &gallery_item_uri);
    bool is_gallery_item_uri_Set() const;
    bool is_gallery_item_uri_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_gallery_item_uri;
    bool m_gallery_item_uri_isSet;
    bool m_gallery_item_uri_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGalleryItemUriPayload)

#endif // OAIGalleryItemUriPayload_H
