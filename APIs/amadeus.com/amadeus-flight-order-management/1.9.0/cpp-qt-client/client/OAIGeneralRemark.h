/**
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGeneralRemark.h
 *
 * 
 */

#ifndef OAIGeneralRemark_H
#define OAIGeneralRemark_H

#include <QJsonObject>

#include "OAIGeneralRemarkType.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGeneralRemark : public OAIObject {
public:
    OAIGeneralRemark();
    OAIGeneralRemark(QString json);
    ~OAIGeneralRemark() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCategory() const;
    void setCategory(const QString &category);
    bool is_category_Set() const;
    bool is_category_Valid() const;

    QList<QString> getFlightOfferIds() const;
    void setFlightOfferIds(const QList<QString> &flight_offer_ids);
    bool is_flight_offer_ids_Set() const;
    bool is_flight_offer_ids_Valid() const;

    OAIGeneralRemarkType getSubType() const;
    void setSubType(const OAIGeneralRemarkType &sub_type);
    bool is_sub_type_Set() const;
    bool is_sub_type_Valid() const;

    QString getText() const;
    void setText(const QString &text);
    bool is_text_Set() const;
    bool is_text_Valid() const;

    QList<QString> getTravelerIds() const;
    void setTravelerIds(const QList<QString> &traveler_ids);
    bool is_traveler_ids_Set() const;
    bool is_traveler_ids_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_category;
    bool m_category_isSet;
    bool m_category_isValid;

    QList<QString> m_flight_offer_ids;
    bool m_flight_offer_ids_isSet;
    bool m_flight_offer_ids_isValid;

    OAIGeneralRemarkType m_sub_type;
    bool m_sub_type_isSet;
    bool m_sub_type_isValid;

    QString m_text;
    bool m_text_isSet;
    bool m_text_isValid;

    QList<QString> m_traveler_ids;
    bool m_traveler_ids_isSet;
    bool m_traveler_ids_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGeneralRemark)

#endif // OAIGeneralRemark_H
