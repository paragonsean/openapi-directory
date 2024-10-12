/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIShipment_TrackingNumber.h
 *
 * 
 */

#ifndef OAIShipment_TrackingNumber_H
#define OAIShipment_TrackingNumber_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIShipment_TrackingNumber : public OAIObject {
public:
    OAIShipment_TrackingNumber();
    OAIShipment_TrackingNumber(QString json);
    ~OAIShipment_TrackingNumber() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getAdditionalFields() const;
    void setAdditionalFields(const OAIObject &additional_fields);
    bool is_additional_fields_Set() const;
    bool is_additional_fields_Valid() const;

    QString getCarrierId() const;
    void setCarrierId(const QString &carrier_id);
    bool is_carrier_id_Set() const;
    bool is_carrier_id_Valid() const;

    OAIObject getCustomFields() const;
    void setCustomFields(const OAIObject &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    QString getTrackingNumber() const;
    void setTrackingNumber(const QString &tracking_number);
    bool is_tracking_number_Set() const;
    bool is_tracking_number_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_additional_fields;
    bool m_additional_fields_isSet;
    bool m_additional_fields_isValid;

    QString m_carrier_id;
    bool m_carrier_id_isSet;
    bool m_carrier_id_isValid;

    OAIObject m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    QString m_tracking_number;
    bool m_tracking_number_isSet;
    bool m_tracking_number_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIShipment_TrackingNumber)

#endif // OAIShipment_TrackingNumber_H
