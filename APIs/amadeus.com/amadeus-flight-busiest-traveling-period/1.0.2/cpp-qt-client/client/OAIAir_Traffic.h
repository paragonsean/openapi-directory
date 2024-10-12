/**
 * Flight Busiest Traveling Period
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAir_Traffic.h
 *
 * 
 */

#ifndef OAIAir_Traffic_H
#define OAIAir_Traffic_H

#include <QJsonObject>

#include "OAIAnalytics.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAnalytics;

class OAIAir_Traffic : public OAIObject {
public:
    OAIAir_Traffic();
    OAIAir_Traffic(QString json);
    ~OAIAir_Traffic() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAnalytics getAnalytics() const;
    void setAnalytics(const OAIAnalytics &analytics);
    bool is_analytics_Set() const;
    bool is_analytics_Valid() const;

    QString getPeriod() const;
    void setPeriod(const QString &period);
    bool is_period_Set() const;
    bool is_period_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAnalytics m_analytics;
    bool m_analytics_isSet;
    bool m_analytics_isValid;

    QString m_period;
    bool m_period_isSet;
    bool m_period_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAir_Traffic)

#endif // OAIAir_Traffic_H
