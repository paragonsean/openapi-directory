/**
 * OpenUV - Global Real-Time UV Index Forecast API
 * The missing minimalistic JSON real-time UV Index API for awesome Developers, Innovators and Smart Home Enthusiasts
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUvIndexResult.h
 *
 * 
 */

#ifndef OAIUvIndexResult_H
#define OAIUvIndexResult_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUvIndexResult : public OAIObject {
public:
    OAIUvIndexResult();
    OAIUvIndexResult(QString json);
    ~OAIUvIndexResult() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getFromTime() const;
    void setFromTime(const QString &from_time);
    bool is_from_time_Set() const;
    bool is_from_time_Valid() const;

    double getFromUv() const;
    void setFromUv(const double &from_uv);
    bool is_from_uv_Set() const;
    bool is_from_uv_Valid() const;

    QString getToTime() const;
    void setToTime(const QString &to_time);
    bool is_to_time_Set() const;
    bool is_to_time_Valid() const;

    double getToUv() const;
    void setToUv(const double &to_uv);
    bool is_to_uv_Set() const;
    bool is_to_uv_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_from_time;
    bool m_from_time_isSet;
    bool m_from_time_isValid;

    double m_from_uv;
    bool m_from_uv_isSet;
    bool m_from_uv_isValid;

    QString m_to_time;
    bool m_to_time_isSet;
    bool m_to_time_isValid;

    double m_to_uv;
    bool m_to_uv_isSet;
    bool m_to_uv_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUvIndexResult)

#endif // OAIUvIndexResult_H
