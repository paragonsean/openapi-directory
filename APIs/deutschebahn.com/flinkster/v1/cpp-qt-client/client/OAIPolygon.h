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
 * OAIPolygon.h
 *
 * 
 */

#ifndef OAIPolygon_H
#define OAIPolygon_H

#include <QJsonObject>

#include "OAICrs.h"
#include "OAIGeoJsonObject.h"
#include "OAILngLatAlt.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICrs;
class OAILngLatAlt;

class OAIPolygon : public OAIObject {
public:
    OAIPolygon();
    OAIPolygon(QString json);
    ~OAIPolygon() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<double> getBbox() const;
    void setBbox(const QList<double> &bbox);
    bool is_bbox_Set() const;
    bool is_bbox_Valid() const;

    OAICrs getCrs() const;
    void setCrs(const OAICrs &crs);
    bool is_crs_Set() const;
    bool is_crs_Valid() const;

    QList<QList<OAILngLatAlt>> getCoordinates() const;
    void setCoordinates(const QList<QList<OAILngLatAlt>> &coordinates);
    bool is_coordinates_Set() const;
    bool is_coordinates_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<double> m_bbox;
    bool m_bbox_isSet;
    bool m_bbox_isValid;

    OAICrs m_crs;
    bool m_crs_isSet;
    bool m_crs_isValid;

    QList<QList<OAILngLatAlt>> m_coordinates;
    bool m_coordinates_isSet;
    bool m_coordinates_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPolygon)

#endif // OAIPolygon_H
