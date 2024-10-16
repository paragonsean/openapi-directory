/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetGalleryPhotosByID_200_response.h
 *
 * 
 */

#ifndef OAIGetGalleryPhotosByID_200_response_H
#define OAIGetGalleryPhotosByID_200_response_H

#include <QJsonObject>

#include "OAIPhoto.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPhoto;

class OAIGetGalleryPhotosByID_200_response : public OAIObject {
public:
    OAIGetGalleryPhotosByID_200_response();
    OAIGetGalleryPhotosByID_200_response(QString json);
    ~OAIGetGalleryPhotosByID_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIPhoto> getPhotos() const;
    void setPhotos(const QList<OAIPhoto> &photos);
    bool is_photos_Set() const;
    bool is_photos_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIPhoto> m_photos;
    bool m_photos_isSet;
    bool m_photos_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetGalleryPhotosByID_200_response)

#endif // OAIGetGalleryPhotosByID_200_response_H
