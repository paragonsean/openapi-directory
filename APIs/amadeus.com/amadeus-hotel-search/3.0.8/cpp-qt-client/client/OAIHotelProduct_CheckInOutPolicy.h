/**
 * Hotel Search API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 3.0.8
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIHotelProduct_CheckInOutPolicy.h
 *
 * 
 */

#ifndef OAIHotelProduct_CheckInOutPolicy_H
#define OAIHotelProduct_CheckInOutPolicy_H

#include <QJsonObject>

#include "OAIQualifiedFreeText.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIQualifiedFreeText;

class OAIHotelProduct_CheckInOutPolicy : public OAIObject {
public:
    OAIHotelProduct_CheckInOutPolicy();
    OAIHotelProduct_CheckInOutPolicy(QString json);
    ~OAIHotelProduct_CheckInOutPolicy() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCheckIn() const;
    void setCheckIn(const QString &check_in);
    bool is_check_in_Set() const;
    bool is_check_in_Valid() const;

    OAIQualifiedFreeText getCheckInDescription() const;
    void setCheckInDescription(const OAIQualifiedFreeText &check_in_description);
    bool is_check_in_description_Set() const;
    bool is_check_in_description_Valid() const;

    QString getCheckOut() const;
    void setCheckOut(const QString &check_out);
    bool is_check_out_Set() const;
    bool is_check_out_Valid() const;

    OAIQualifiedFreeText getCheckOutDescription() const;
    void setCheckOutDescription(const OAIQualifiedFreeText &check_out_description);
    bool is_check_out_description_Set() const;
    bool is_check_out_description_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_check_in;
    bool m_check_in_isSet;
    bool m_check_in_isValid;

    OAIQualifiedFreeText m_check_in_description;
    bool m_check_in_description_isSet;
    bool m_check_in_description_isValid;

    QString m_check_out;
    bool m_check_out_isSet;
    bool m_check_out_isValid;

    OAIQualifiedFreeText m_check_out_description;
    bool m_check_out_description_isSet;
    bool m_check_out_description_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHotelProduct_CheckInOutPolicy)

#endif // OAIHotelProduct_CheckInOutPolicy_H
