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
 * OAICarVehicle.h
 *
 * 
 */

#ifndef OAICarVehicle_H
#define OAICarVehicle_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICarVehicle : public OAIObject {
public:
    OAICarVehicle();
    OAICarVehicle(QString json);
    ~OAICarVehicle() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAcrissCode() const;
    void setAcrissCode(const QString &acriss_code);
    bool is_acriss_code_Set() const;
    bool is_acriss_code_Valid() const;

    QString getCarModel() const;
    void setCarModel(const QString &car_model);
    bool is_car_model_Set() const;
    bool is_car_model_Valid() const;

    qint32 getDoors() const;
    void setDoors(const qint32 &doors);
    bool is_doors_Set() const;
    bool is_doors_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_acriss_code;
    bool m_acriss_code_isSet;
    bool m_acriss_code_isValid;

    QString m_car_model;
    bool m_car_model_isSet;
    bool m_car_model_isValid;

    qint32 m_doors;
    bool m_doors_isSet;
    bool m_doors_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICarVehicle)

#endif // OAICarVehicle_H
