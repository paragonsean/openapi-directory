/**
 * Cloud-RF API
 * Use this JSON API to build and test radio links for any radio, anywhere. Authenticate with your API2.0 key in the request header as key
 *
 * The version of the OpenAPI document: 2.0.0
 * Contact: support@cloudrf.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIReceiver.h
 *
 * 
 */

#ifndef OAIReceiver_H
#define OAIReceiver_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIReceiver : public OAIObject {
public:
    OAIReceiver();
    OAIReceiver(QString json);
    ~OAIReceiver() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    float getAlt() const;
    void setAlt(const float &alt);
    bool is_alt_Set() const;
    bool is_alt_Valid() const;

    float getLat() const;
    void setLat(const float &lat);
    bool is_lat_Set() const;
    bool is_lat_Valid() const;

    float getLon() const;
    void setLon(const float &lon);
    bool is_lon_Set() const;
    bool is_lon_Valid() const;

    float getRxg() const;
    void setRxg(const float &rxg);
    bool is_rxg_Set() const;
    bool is_rxg_Valid() const;

    float getRxs() const;
    void setRxs(const float &rxs);
    bool is_rxs_Set() const;
    bool is_rxs_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    float m_alt;
    bool m_alt_isSet;
    bool m_alt_isValid;

    float m_lat;
    bool m_lat_isSet;
    bool m_lat_isValid;

    float m_lon;
    bool m_lon_isSet;
    bool m_lon_isValid;

    float m_rxg;
    bool m_rxg_isSet;
    bool m_rxg_isValid;

    float m_rxs;
    bool m_rxs_isSet;
    bool m_rxs_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIReceiver)

#endif // OAIReceiver_H
