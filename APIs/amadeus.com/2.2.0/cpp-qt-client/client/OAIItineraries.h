/**
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIItineraries.h
 *
 * 
 */

#ifndef OAIItineraries_H
#define OAIItineraries_H

#include <QJsonObject>

#include "OAISegment.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISegment;

class OAIItineraries : public OAIObject {
public:
    OAIItineraries();
    OAIItineraries(QString json);
    ~OAIItineraries() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDuration() const;
    void setDuration(const QString &duration);
    bool is_duration_Set() const;
    bool is_duration_Valid() const;

    QList<OAISegment> getSegments() const;
    void setSegments(const QList<OAISegment> &segments);
    bool is_segments_Set() const;
    bool is_segments_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_duration;
    bool m_duration_isSet;
    bool m_duration_isValid;

    QList<OAISegment> m_segments;
    bool m_segments_isSet;
    bool m_segments_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIItineraries)

#endif // OAIItineraries_H
