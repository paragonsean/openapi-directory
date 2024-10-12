/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITemando_shipping_data_collection_point_search_request_interface.h
 *
 * Temando Collection Point Search Request Interface
 */

#ifndef OAITemando_shipping_data_collection_point_search_request_interface_H
#define OAITemando_shipping_data_collection_point_search_request_interface_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITemando_shipping_data_collection_point_search_request_interface : public OAIObject {
public:
    OAITemando_shipping_data_collection_point_search_request_interface();
    OAITemando_shipping_data_collection_point_search_request_interface(QString json);
    ~OAITemando_shipping_data_collection_point_search_request_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCountryId() const;
    void setCountryId(const QString &country_id);
    bool is_country_id_Set() const;
    bool is_country_id_Valid() const;

    bool isPending() const;
    void setPending(const bool &pending);
    bool is_pending_Set() const;
    bool is_pending_Valid() const;

    QString getPostcode() const;
    void setPostcode(const QString &postcode);
    bool is_postcode_Set() const;
    bool is_postcode_Valid() const;

    qint32 getShippingAddressId() const;
    void setShippingAddressId(const qint32 &shipping_address_id);
    bool is_shipping_address_id_Set() const;
    bool is_shipping_address_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_country_id;
    bool m_country_id_isSet;
    bool m_country_id_isValid;

    bool m_pending;
    bool m_pending_isSet;
    bool m_pending_isValid;

    QString m_postcode;
    bool m_postcode_isSet;
    bool m_postcode_isValid;

    qint32 m_shipping_address_id;
    bool m_shipping_address_id_isSet;
    bool m_shipping_address_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITemando_shipping_data_collection_point_search_request_interface)

#endif // OAITemando_shipping_data_collection_point_search_request_interface_H
