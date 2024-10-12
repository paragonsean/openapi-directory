/**
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAI_conversations__conversation_id__offer_post_request.h
 *
 * 
 */

#ifndef OAI_conversations__conversation_id__offer_post_request_H
#define OAI_conversations__conversation_id__offer_post_request_H

#include <QJsonObject>

#include "OAI_conversations__conversation_id__offer_post_request_offer_items_inner.h"
#include "OAI_conversations__conversation_id__offer_post_request_price.h"
#include "OAI_conversations__conversation_id__offer_post_request_shipping_price.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAI_conversations__conversation_id__offer_post_request_offer_items_inner;
class OAI_conversations__conversation_id__offer_post_request_price;
class OAI_conversations__conversation_id__offer_post_request_shipping_price;

class OAI_conversations__conversation_id__offer_post_request : public OAIObject {
public:
    OAI_conversations__conversation_id__offer_post_request();
    OAI_conversations__conversation_id__offer_post_request(QString json);
    ~OAI_conversations__conversation_id__offer_post_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCountryCode() const;
    void setCountryCode(const QString &country_code);
    bool is_country_code_Set() const;
    bool is_country_code_Valid() const;

    QString getLayawayTermsSlug() const;
    void setLayawayTermsSlug(const QString &layaway_terms_slug);
    bool is_layaway_terms_slug_Set() const;
    bool is_layaway_terms_slug_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    QList<OAI_conversations__conversation_id__offer_post_request_offer_items_inner> getOfferItems() const;
    void setOfferItems(const QList<OAI_conversations__conversation_id__offer_post_request_offer_items_inner> &offer_items);
    bool is_offer_items_Set() const;
    bool is_offer_items_Valid() const;

    OAI_conversations__conversation_id__offer_post_request_price getPrice() const;
    void setPrice(const OAI_conversations__conversation_id__offer_post_request_price &price);
    bool is_price_Set() const;
    bool is_price_Valid() const;

    QString getQuantity() const;
    void setQuantity(const QString &quantity);
    bool is_quantity_Set() const;
    bool is_quantity_Valid() const;

    QString getRecipientId() const;
    void setRecipientId(const QString &recipient_id);
    bool is_recipient_id_Set() const;
    bool is_recipient_id_Valid() const;

    QString getRegionCode() const;
    void setRegionCode(const QString &region_code);
    bool is_region_code_Set() const;
    bool is_region_code_Valid() const;

    OAI_conversations__conversation_id__offer_post_request_shipping_price getShippingPrice() const;
    void setShippingPrice(const OAI_conversations__conversation_id__offer_post_request_shipping_price &shipping_price);
    bool is_shipping_price_Set() const;
    bool is_shipping_price_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_country_code;
    bool m_country_code_isSet;
    bool m_country_code_isValid;

    QString m_layaway_terms_slug;
    bool m_layaway_terms_slug_isSet;
    bool m_layaway_terms_slug_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    QList<OAI_conversations__conversation_id__offer_post_request_offer_items_inner> m_offer_items;
    bool m_offer_items_isSet;
    bool m_offer_items_isValid;

    OAI_conversations__conversation_id__offer_post_request_price m_price;
    bool m_price_isSet;
    bool m_price_isValid;

    QString m_quantity;
    bool m_quantity_isSet;
    bool m_quantity_isValid;

    QString m_recipient_id;
    bool m_recipient_id_isSet;
    bool m_recipient_id_isValid;

    QString m_region_code;
    bool m_region_code_isSet;
    bool m_region_code_isValid;

    OAI_conversations__conversation_id__offer_post_request_shipping_price m_shipping_price;
    bool m_shipping_price_isSet;
    bool m_shipping_price_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_conversations__conversation_id__offer_post_request)

#endif // OAI_conversations__conversation_id__offer_post_request_H
