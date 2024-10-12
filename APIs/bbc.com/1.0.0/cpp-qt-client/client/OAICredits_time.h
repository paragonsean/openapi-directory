/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICredits_time.h
 *
 * 
 */

#ifndef OAICredits_time_H
#define OAICredits_time_H

#include <QJsonObject>

#include <QDateTime>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICredits_time : public OAIObject {
public:
    OAICredits_time();
    OAICredits_time(QString json);
    ~OAICredits_time() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getSqueezeEnd() const;
    void setSqueezeEnd(const QDateTime &squeeze_end);
    bool is_squeeze_end_Set() const;
    bool is_squeeze_end_Valid() const;

    QDateTime getSqueezeStart() const;
    void setSqueezeStart(const QDateTime &squeeze_start);
    bool is_squeeze_start_Set() const;
    bool is_squeeze_start_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_squeeze_end;
    bool m_squeeze_end_isSet;
    bool m_squeeze_end_isValid;

    QDateTime m_squeeze_start;
    bool m_squeeze_start_isSet;
    bool m_squeeze_start_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICredits_time)

#endif // OAICredits_time_H
