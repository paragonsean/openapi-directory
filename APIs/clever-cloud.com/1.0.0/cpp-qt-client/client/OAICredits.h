/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICredits.h
 *
 * 
 */

#ifndef OAICredits_H
#define OAICredits_H

#include <QJsonObject>

#include "OAICredits_dropPrice.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICredits_dropPrice;

class OAICredits : public OAIObject {
public:
    OAICredits();
    OAICredits(QString json);
    ~OAICredits() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    float getCount() const;
    void setCount(const float &count);
    bool is_count_Set() const;
    bool is_count_Valid() const;

    OAICredits_dropPrice getDropPrice() const;
    void setDropPrice(const OAICredits_dropPrice &drop_price);
    bool is_drop_price_Set() const;
    bool is_drop_price_Valid() const;

    QString getOwnerId() const;
    void setOwnerId(const QString &owner_id);
    bool is_owner_id_Set() const;
    bool is_owner_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    float m_count;
    bool m_count_isSet;
    bool m_count_isValid;

    OAICredits_dropPrice m_drop_price;
    bool m_drop_price_isSet;
    bool m_drop_price_isValid;

    QString m_owner_id;
    bool m_owner_id_isSet;
    bool m_owner_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICredits)

#endif // OAICredits_H
