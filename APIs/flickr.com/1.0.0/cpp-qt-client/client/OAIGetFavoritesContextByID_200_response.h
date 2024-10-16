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
 * OAIGetFavoritesContextByID_200_response.h
 *
 * 
 */

#ifndef OAIGetFavoritesContextByID_200_response_H
#define OAIGetFavoritesContextByID_200_response_H

#include <QJsonObject>

#include "OAIContextPhoto.h"
#include "OAIGetFavoritesContextByID_200_response_count.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetFavoritesContextByID_200_response_count;
class OAIContextPhoto;

class OAIGetFavoritesContextByID_200_response : public OAIObject {
public:
    OAIGetFavoritesContextByID_200_response();
    OAIGetFavoritesContextByID_200_response(QString json);
    ~OAIGetFavoritesContextByID_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGetFavoritesContextByID_200_response_count getCount() const;
    void setCount(const OAIGetFavoritesContextByID_200_response_count &count);
    bool is_count_Set() const;
    bool is_count_Valid() const;

    OAIContextPhoto getNextphoto() const;
    void setNextphoto(const OAIContextPhoto &nextphoto);
    bool is_nextphoto_Set() const;
    bool is_nextphoto_Valid() const;

    OAIContextPhoto getPrevphoto() const;
    void setPrevphoto(const OAIContextPhoto &prevphoto);
    bool is_prevphoto_Set() const;
    bool is_prevphoto_Valid() const;

    QString getStat() const;
    void setStat(const QString &stat);
    bool is_stat_Set() const;
    bool is_stat_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGetFavoritesContextByID_200_response_count m_count;
    bool m_count_isSet;
    bool m_count_isValid;

    OAIContextPhoto m_nextphoto;
    bool m_nextphoto_isSet;
    bool m_nextphoto_isValid;

    OAIContextPhoto m_prevphoto;
    bool m_prevphoto_isSet;
    bool m_prevphoto_isValid;

    QString m_stat;
    bool m_stat_isSet;
    bool m_stat_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetFavoritesContextByID_200_response)

#endif // OAIGetFavoritesContextByID_200_response_H
