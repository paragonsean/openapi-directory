/**
 * Flinkster_API_NG
 * This REST-API enables you to query for private transport sharing offers provided by companies and cities in Germany, Netherland and Austria.  You can search for informations about the rental stations (points or areas) where you can find the rentals by utilizing the /areas/ ressource.  With the help of the proximity search in the /bookingproposals/ URI you can request the availabilities of the rentalobjects for spontaneous or planed usage in the future.   Feel free to browse through data by setting the parameter 'providernetwork' to the value:   1: Search for car sharing offers provided by the Flinkster platform (http://www.flinkster.de) 2: Finding bike rental offers from Call a Bike (http://www.callabike.de)   You can find more details in the documentation section (Unfortunately only available in german language).  Have lots of fun and we are lucky to take notice of your products or getting your feedback.
 *
 * The version of the OpenAPI document: v1
 * Contact: partner@flinkster.de
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRentalObjectJO.h
 *
 * 
 */

#ifndef OAIRentalObjectJO_H
#define OAIRentalObjectJO_H

#include <QJsonObject>

#include "OAICategoryJO.h"
#include "OAILinkJO.h"
#include "OAIObject.h"
#include "OAIProviderJO.h"
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILinkJO;
class OAICategoryJO;
class OAIProviderJO;

class OAIRentalObjectJO : public OAIObject {
public:
    OAIRentalObjectJO();
    OAIRentalObjectJO(QString json);
    ~OAIRentalObjectJO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAILinkJO> getLinks() const;
    void setLinks(const QList<OAILinkJO> &_links);
    bool is__links_Set() const;
    bool is__links_Valid() const;

    QMap<QString, OAIObject> getAttributes() const;
    void setAttributes(const QMap<QString, OAIObject> &attributes);
    bool is_attributes_Set() const;
    bool is_attributes_Valid() const;

    OAICategoryJO getCategory() const;
    void setCategory(const OAICategoryJO &category);
    bool is_category_Set() const;
    bool is_category_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getExpand() const;
    void setExpand(const QString &expand);
    bool is_expand_Set() const;
    bool is_expand_Valid() const;

    QString getHref() const;
    void setHref(const QString &href);
    bool is_href_Set() const;
    bool is_href_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    OAIProviderJO getProvider() const;
    void setProvider(const OAIProviderJO &provider);
    bool is_provider_Set() const;
    bool is_provider_Valid() const;

    QList<qint32> getProviderNetworkIds() const;
    void setProviderNetworkIds(const QList<qint32> &provider_network_ids);
    bool is_provider_network_ids_Set() const;
    bool is_provider_network_ids_Valid() const;

    QString getProviderRentalObjectId() const;
    void setProviderRentalObjectId(const QString &provider_rental_object_id);
    bool is_provider_rental_object_id_Set() const;
    bool is_provider_rental_object_id_Valid() const;

    QString getRentalModel() const;
    void setRentalModel(const QString &rental_model);
    bool is_rental_model_Set() const;
    bool is_rental_model_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getUid() const;
    void setUid(const QString &uid);
    bool is_uid_Set() const;
    bool is_uid_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAILinkJO> m__links;
    bool m__links_isSet;
    bool m__links_isValid;

    QMap<QString, OAIObject> m_attributes;
    bool m_attributes_isSet;
    bool m_attributes_isValid;

    OAICategoryJO m_category;
    bool m_category_isSet;
    bool m_category_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_expand;
    bool m_expand_isSet;
    bool m_expand_isValid;

    QString m_href;
    bool m_href_isSet;
    bool m_href_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    OAIProviderJO m_provider;
    bool m_provider_isSet;
    bool m_provider_isValid;

    QList<qint32> m_provider_network_ids;
    bool m_provider_network_ids_isSet;
    bool m_provider_network_ids_isValid;

    QString m_provider_rental_object_id;
    bool m_provider_rental_object_id_isSet;
    bool m_provider_rental_object_id_isValid;

    QString m_rental_model;
    bool m_rental_model_isSet;
    bool m_rental_model_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_uid;
    bool m_uid_isSet;
    bool m_uid_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRentalObjectJO)

#endif // OAIRentalObjectJO_H
