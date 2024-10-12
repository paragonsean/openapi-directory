/**
 * Azure Media Services
 * This Swagger was generated by the API Framework.
 *
 * The version of the OpenAPI document: 2018-07-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIMediaFilterProperties.h
 *
 * The Media Filter properties.
 */

#ifndef OAIMediaFilterProperties_H
#define OAIMediaFilterProperties_H

#include <QJsonObject>

#include "OAIFilterTrackSelection.h"
#include "OAIFirstQuality.h"
#include "OAIPresentationTimeRange.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFirstQuality;
class OAIPresentationTimeRange;
class OAIFilterTrackSelection;

class OAIMediaFilterProperties : public OAIObject {
public:
    OAIMediaFilterProperties();
    OAIMediaFilterProperties(QString json);
    ~OAIMediaFilterProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIFirstQuality getFirstQuality() const;
    void setFirstQuality(const OAIFirstQuality &first_quality);
    bool is_first_quality_Set() const;
    bool is_first_quality_Valid() const;

    OAIPresentationTimeRange getPresentationTimeRange() const;
    void setPresentationTimeRange(const OAIPresentationTimeRange &presentation_time_range);
    bool is_presentation_time_range_Set() const;
    bool is_presentation_time_range_Valid() const;

    QList<OAIFilterTrackSelection> getTracks() const;
    void setTracks(const QList<OAIFilterTrackSelection> &tracks);
    bool is_tracks_Set() const;
    bool is_tracks_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIFirstQuality m_first_quality;
    bool m_first_quality_isSet;
    bool m_first_quality_isValid;

    OAIPresentationTimeRange m_presentation_time_range;
    bool m_presentation_time_range_isSet;
    bool m_presentation_time_range_isValid;

    QList<OAIFilterTrackSelection> m_tracks;
    bool m_tracks_isSet;
    bool m_tracks_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIMediaFilterProperties)

#endif // OAIMediaFilterProperties_H
