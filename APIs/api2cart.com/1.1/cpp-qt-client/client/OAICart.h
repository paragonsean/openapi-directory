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
 * OAICart.h
 *
 * 
 */

#ifndef OAICart_H
#define OAICart_H

#include <QJsonObject>

#include "OAICart_ShippingZone.h"
#include "OAICart_StoreInfo.h"
#include "OAICart_Warehouse.h"
#include "OAIObject.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICart_ShippingZone;
class OAICart_StoreInfo;
class OAICart_Warehouse;

class OAICart : public OAIObject {
public:
    OAICart();
    OAICart(QString json);
    ~OAICart() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getAdditionalFields() const;
    void setAdditionalFields(const OAIObject &additional_fields);
    bool is_additional_fields_Set() const;
    bool is_additional_fields_Valid() const;

    OAIObject getCustomFields() const;
    void setCustomFields(const OAIObject &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    QString getDbPrefix() const;
    void setDbPrefix(const QString &db_prefix);
    bool is_db_prefix_Set() const;
    bool is_db_prefix_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<OAICart_ShippingZone> getShippingZones() const;
    void setShippingZones(const QList<OAICart_ShippingZone> &shipping_zones);
    bool is_shipping_zones_Set() const;
    bool is_shipping_zones_Valid() const;

    QList<OAICart_StoreInfo> getStoresInfo() const;
    void setStoresInfo(const QList<OAICart_StoreInfo> &stores_info);
    bool is_stores_info_Set() const;
    bool is_stores_info_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    QString getVersion() const;
    void setVersion(const QString &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    QList<OAICart_Warehouse> getWarehouses() const;
    void setWarehouses(const QList<OAICart_Warehouse> &warehouses);
    bool is_warehouses_Set() const;
    bool is_warehouses_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_additional_fields;
    bool m_additional_fields_isSet;
    bool m_additional_fields_isValid;

    OAIObject m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    QString m_db_prefix;
    bool m_db_prefix_isSet;
    bool m_db_prefix_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<OAICart_ShippingZone> m_shipping_zones;
    bool m_shipping_zones_isSet;
    bool m_shipping_zones_isValid;

    QList<OAICart_StoreInfo> m_stores_info;
    bool m_stores_info_isSet;
    bool m_stores_info_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;

    QString m_version;
    bool m_version_isSet;
    bool m_version_isValid;

    QList<OAICart_Warehouse> m_warehouses;
    bool m_warehouses_isSet;
    bool m_warehouses_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICart)

#endif // OAICart_H
