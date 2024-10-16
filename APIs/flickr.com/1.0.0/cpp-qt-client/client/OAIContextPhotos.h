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
 * OAIContextPhotos.h
 *
 * 
 */

#ifndef OAIContextPhotos_H
#define OAIContextPhotos_H

#include <QJsonObject>

#include "OAIContextPhoto.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIContextPhoto;

class OAIContextPhotos : public OAIObject {
public:
    OAIContextPhotos();
    OAIContextPhotos(QString json);
    ~OAIContextPhotos() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIContextPhoto> getPhotos() const;
    void setPhotos(const QList<OAIContextPhoto> &photos);
    bool is_photos_Set() const;
    bool is_photos_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIContextPhoto> m_photos;
    bool m_photos_isSet;
    bool m_photos_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIContextPhotos)

#endif // OAIContextPhotos_H
