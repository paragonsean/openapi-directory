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
 * OAIFareDetailsBySegment.h
 *
 * Fare details of the segment
 */

#ifndef OAIFareDetailsBySegment_H
#define OAIFareDetailsBySegment_H

#include <QJsonObject>

#include "OAIAdditionalServicesRequest.h"
#include "OAIAllotmentDetails.h"
#include "OAIBaggageAllowance.h"
#include "OAISliceDiceIndicator.h"
#include "OAITravelClass.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAdditionalServicesRequest;
class OAIAllotmentDetails;
class OAIBaggageAllowance;

class OAIFareDetailsBySegment : public OAIObject {
public:
    OAIFareDetailsBySegment();
    OAIFareDetailsBySegment(QString json);
    ~OAIFareDetailsBySegment() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAdditionalServicesRequest getAdditionalServices() const;
    void setAdditionalServices(const OAIAdditionalServicesRequest &additional_services);
    bool is_additional_services_Set() const;
    bool is_additional_services_Valid() const;

    OAIAllotmentDetails getAllotmentDetails() const;
    void setAllotmentDetails(const OAIAllotmentDetails &allotment_details);
    bool is_allotment_details_Set() const;
    bool is_allotment_details_Valid() const;

    QString getBrandedFare() const;
    void setBrandedFare(const QString &branded_fare);
    bool is_branded_fare_Set() const;
    bool is_branded_fare_Valid() const;

    OAITravelClass getCabin() const;
    void setCabin(const OAITravelClass &cabin);
    bool is_cabin_Set() const;
    bool is_cabin_Valid() const;

    QString getRClass() const;
    void setRClass(const QString &r_class);
    bool is_r_class_Set() const;
    bool is_r_class_Valid() const;

    QString getFareBasis() const;
    void setFareBasis(const QString &fare_basis);
    bool is_fare_basis_Set() const;
    bool is_fare_basis_Valid() const;

    OAIBaggageAllowance getIncludedCheckedBags() const;
    void setIncludedCheckedBags(const OAIBaggageAllowance &included_checked_bags);
    bool is_included_checked_bags_Set() const;
    bool is_included_checked_bags_Valid() const;

    bool isIsAllotment() const;
    void setIsAllotment(const bool &is_allotment);
    bool is_is_allotment_Set() const;
    bool is_is_allotment_Valid() const;

    QString getSegmentId() const;
    void setSegmentId(const QString &segment_id);
    bool is_segment_id_Set() const;
    bool is_segment_id_Valid() const;

    OAISliceDiceIndicator getSliceDiceIndicator() const;
    void setSliceDiceIndicator(const OAISliceDiceIndicator &slice_dice_indicator);
    bool is_slice_dice_indicator_Set() const;
    bool is_slice_dice_indicator_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAdditionalServicesRequest m_additional_services;
    bool m_additional_services_isSet;
    bool m_additional_services_isValid;

    OAIAllotmentDetails m_allotment_details;
    bool m_allotment_details_isSet;
    bool m_allotment_details_isValid;

    QString m_branded_fare;
    bool m_branded_fare_isSet;
    bool m_branded_fare_isValid;

    OAITravelClass m_cabin;
    bool m_cabin_isSet;
    bool m_cabin_isValid;

    QString m_r_class;
    bool m_r_class_isSet;
    bool m_r_class_isValid;

    QString m_fare_basis;
    bool m_fare_basis_isSet;
    bool m_fare_basis_isValid;

    OAIBaggageAllowance m_included_checked_bags;
    bool m_included_checked_bags_isSet;
    bool m_included_checked_bags_isValid;

    bool m_is_allotment;
    bool m_is_allotment_isSet;
    bool m_is_allotment_isValid;

    QString m_segment_id;
    bool m_segment_id_isSet;
    bool m_segment_id_isValid;

    OAISliceDiceIndicator m_slice_dice_indicator;
    bool m_slice_dice_indicator_isSet;
    bool m_slice_dice_indicator_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFareDetailsBySegment)

#endif // OAIFareDetailsBySegment_H
