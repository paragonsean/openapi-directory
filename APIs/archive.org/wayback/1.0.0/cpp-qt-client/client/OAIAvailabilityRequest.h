/**
 * Wayback API
 * API for Internet Archive's Wayback Machine
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAvailabilityRequest.h
 *
 * 
 */

#ifndef OAIAvailabilityRequest_H
#define OAIAvailabilityRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAvailabilityRequest : public OAIObject {
public:
    OAIAvailabilityRequest();
    OAIAvailabilityRequest(QString json);
    ~OAIAvailabilityRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getClosest() const;
    void setClosest(const QString &closest);
    bool is_closest_Set() const;
    bool is_closest_Valid() const;

    QString getTag() const;
    void setTag(const QString &tag);
    bool is_tag_Set() const;
    bool is_tag_Valid() const;

    QString getTimestamp() const;
    void setTimestamp(const QString &timestamp);
    bool is_timestamp_Set() const;
    bool is_timestamp_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_closest;
    bool m_closest_isSet;
    bool m_closest_isValid;

    QString m_tag;
    bool m_tag_isSet;
    bool m_tag_isValid;

    QString m_timestamp;
    bool m_timestamp_isSet;
    bool m_timestamp_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAvailabilityRequest)

#endif // OAIAvailabilityRequest_H
