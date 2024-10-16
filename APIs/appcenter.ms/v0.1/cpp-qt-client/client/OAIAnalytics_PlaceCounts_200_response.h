/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAnalytics_PlaceCounts_200_response.h
 *
 * Places and count during the time range in descending order.
 */

#ifndef OAIAnalytics_PlaceCounts_200_response_H
#define OAIAnalytics_PlaceCounts_200_response_H

#include <QJsonObject>

#include "OAIAnalytics_PlaceCounts_200_response_places_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAnalytics_PlaceCounts_200_response_places_inner;

class OAIAnalytics_PlaceCounts_200_response : public OAIObject {
public:
    OAIAnalytics_PlaceCounts_200_response();
    OAIAnalytics_PlaceCounts_200_response(QString json);
    ~OAIAnalytics_PlaceCounts_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIAnalytics_PlaceCounts_200_response_places_inner> getPlaces() const;
    void setPlaces(const QList<OAIAnalytics_PlaceCounts_200_response_places_inner> &places);
    bool is_places_Set() const;
    bool is_places_Valid() const;

    qint64 getTotal() const;
    void setTotal(const qint64 &total);
    bool is_total_Set() const;
    bool is_total_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIAnalytics_PlaceCounts_200_response_places_inner> m_places;
    bool m_places_isSet;
    bool m_places_isValid;

    qint64 m_total;
    bool m_total_isSet;
    bool m_total_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAnalytics_PlaceCounts_200_response)

#endif // OAIAnalytics_PlaceCounts_200_response_H
