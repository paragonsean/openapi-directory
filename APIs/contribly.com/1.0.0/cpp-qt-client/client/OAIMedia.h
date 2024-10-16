/**
 * Contribly
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIMedia.h
 *
 * 
 */

#ifndef OAIMedia_H
#define OAIMedia_H

#include <QJsonObject>

#include "OAIPlace.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPlace;

class OAIMedia : public OAIObject {
public:
    OAIMedia();
    OAIMedia(QString json);
    ~OAIMedia() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getDuration() const;
    void setDuration(const double &duration);
    bool is_duration_Set() const;
    bool is_duration_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    OAIPlace getPlace() const;
    void setPlace(const OAIPlace &place);
    bool is_place_Set() const;
    bool is_place_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_duration;
    bool m_duration_isSet;
    bool m_duration_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAIPlace m_place;
    bool m_place_isSet;
    bool m_place_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIMedia)

#endif // OAIMedia_H
