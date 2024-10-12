/**
 * Azure Media Services
 * This Swagger was generated by the API Framework.
 *
 * The version of the OpenAPI document: 2018-07-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFirstQuality.h
 *
 * Filter First Quality
 */

#ifndef OAIFirstQuality_H
#define OAIFirstQuality_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFirstQuality : public OAIObject {
public:
    OAIFirstQuality();
    OAIFirstQuality(QString json);
    ~OAIFirstQuality() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getBitrate() const;
    void setBitrate(const qint32 &bitrate);
    bool is_bitrate_Set() const;
    bool is_bitrate_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_bitrate;
    bool m_bitrate_isSet;
    bool m_bitrate_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFirstQuality)

#endif // OAIFirstQuality_H
