/**
 * Trip Parser
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 3.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDropoff.h
 *
 * dropoff location and time of the rented vehicle.
 */

#ifndef OAIDropoff_H
#define OAIDropoff_H

#include <QJsonObject>

#include "OAILocation.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILocation;

class OAIDropoff : public OAIObject {
public:
    OAIDropoff();
    OAIDropoff(QString json);
    ~OAIDropoff() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getLocalDateTime() const;
    void setLocalDateTime(const QString &local_date_time);
    bool is_local_date_time_Set() const;
    bool is_local_date_time_Valid() const;

    OAILocation getLocation() const;
    void setLocation(const OAILocation &location);
    bool is_location_Set() const;
    bool is_location_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_local_date_time;
    bool m_local_date_time_isSet;
    bool m_local_date_time_isValid;

    OAILocation m_location;
    bool m_location_isSet;
    bool m_location_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDropoff)

#endif // OAIDropoff_H
