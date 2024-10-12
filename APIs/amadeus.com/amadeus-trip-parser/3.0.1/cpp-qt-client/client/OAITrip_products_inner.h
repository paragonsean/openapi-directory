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
 * OAITrip_products_inner.h
 *
 * 
 */

#ifndef OAITrip_products_inner_H
#define OAITrip_products_inner_H

#include <QJsonObject>

#include "OAIAir.h"
#include "OAIAirData.h"
#include "OAICar.h"
#include "OAICarData.h"
#include "OAIHotel.h"
#include "OAIHotelData.h"
#include "OAITrain.h"
#include "OAITrainData.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAirData;
class OAIHotelData;
class OAICarData;
class OAITrainData;

class OAITrip_products_inner : public OAIObject {
public:
    OAITrip_products_inner();
    OAITrip_products_inner(QString json);
    ~OAITrip_products_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAirData getAir() const;
    void setAir(const OAIAirData &air);
    bool is_air_Set() const;
    bool is_air_Valid() const;

    OAIHotelData getHotel() const;
    void setHotel(const OAIHotelData &hotel);
    bool is_hotel_Set() const;
    bool is_hotel_Valid() const;

    OAICarData getCar() const;
    void setCar(const OAICarData &car);
    bool is_car_Set() const;
    bool is_car_Valid() const;

    OAITrainData getTrain() const;
    void setTrain(const OAITrainData &train);
    bool is_train_Set() const;
    bool is_train_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAirData m_air;
    bool m_air_isSet;
    bool m_air_isValid;

    OAIHotelData m_hotel;
    bool m_hotel_isSet;
    bool m_hotel_isValid;

    OAICarData m_car;
    bool m_car_isSet;
    bool m_car_isValid;

    OAITrainData m_train;
    bool m_train_isSet;
    bool m_train_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITrip_products_inner)

#endif // OAITrip_products_inner_H
