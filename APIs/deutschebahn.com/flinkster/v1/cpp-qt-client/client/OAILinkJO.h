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
 * OAILinkJO.h
 *
 * 
 */

#ifndef OAILinkJO_H
#define OAILinkJO_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAILinkJO : public OAIObject {
public:
    OAILinkJO();
    OAILinkJO(QString json);
    ~OAILinkJO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getHref() const;
    void setHref(const QString &href);
    bool is_href_Set() const;
    bool is_href_Valid() const;

    QString getRel() const;
    void setRel(const QString &rel);
    bool is_rel_Set() const;
    bool is_rel_Valid() const;

    QString getVerb() const;
    void setVerb(const QString &verb);
    bool is_verb_Set() const;
    bool is_verb_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_href;
    bool m_href_isSet;
    bool m_href_isValid;

    QString m_rel;
    bool m_rel_isSet;
    bool m_rel_isValid;

    QString m_verb;
    bool m_verb_isSet;
    bool m_verb_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILinkJO)

#endif // OAILinkJO_H
