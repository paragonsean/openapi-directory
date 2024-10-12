/**
 * Highways England API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIQualities.h
 *
 * 
 */

#ifndef OAIQualities_H
#define OAIQualities_H

#include <QJsonObject>

#include <QDateTime>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIQualities : public OAIObject {
public:
    OAIQualities();
    OAIQualities(QString json);
    ~OAIQualities() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getDate() const;
    void setDate(const QDateTime &date);
    bool is_date_Set() const;
    bool is_date_Valid() const;

    qint32 getQuality() const;
    void setQuality(const qint32 &quality);
    bool is_quality_Set() const;
    bool is_quality_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_date;
    bool m_date_isSet;
    bool m_date_isValid;

    qint32 m_quality;
    bool m_quality_isSet;
    bool m_quality_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIQualities)

#endif // OAIQualities_H
