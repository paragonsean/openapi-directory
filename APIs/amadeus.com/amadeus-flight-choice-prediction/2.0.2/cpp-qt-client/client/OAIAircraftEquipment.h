/**
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAircraftEquipment.h
 *
 * information related to the aircraft
 */

#ifndef OAIAircraftEquipment_H
#define OAIAircraftEquipment_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAircraftEquipment : public OAIObject {
public:
    OAIAircraftEquipment();
    OAIAircraftEquipment(QString json);
    ~OAIAircraftEquipment() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    QString getConfigurationVersion() const;
    void setConfigurationVersion(const QString &configuration_version);
    bool is_configuration_version_Set() const;
    bool is_configuration_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    QString m_configuration_version;
    bool m_configuration_version_isSet;
    bool m_configuration_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAircraftEquipment)

#endif // OAIAircraftEquipment_H
