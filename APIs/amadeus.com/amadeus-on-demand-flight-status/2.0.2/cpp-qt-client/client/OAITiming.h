/**
 * On-Demand Flight Status
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.     Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITiming.h
 *
 * 
 */

#ifndef OAITiming_H
#define OAITiming_H

#include <QJsonObject>

#include "OAIDelay.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDelay;

class OAITiming : public OAIObject {
public:
    OAITiming();
    OAITiming(QString json);
    ~OAITiming() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIDelay> getDelays() const;
    void setDelays(const QList<OAIDelay> &delays);
    bool is_delays_Set() const;
    bool is_delays_Valid() const;

    QString getQualifier() const;
    void setQualifier(const QString &qualifier);
    bool is_qualifier_Set() const;
    bool is_qualifier_Valid() const;

    QDateTime getValue() const;
    void setValue(const QDateTime &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIDelay> m_delays;
    bool m_delays_isSet;
    bool m_delays_isValid;

    QString m_qualifier;
    bool m_qualifier_isSet;
    bool m_qualifier_isValid;

    QDateTime m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITiming)

#endif // OAITiming_H
