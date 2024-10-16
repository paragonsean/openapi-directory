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
 * OAIOsmId.h
 *
 * 
 */

#ifndef OAIOsmId_H
#define OAIOsmId_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIOsmId : public OAIObject {
public:
    OAIOsmId();
    OAIOsmId(QString json);
    ~OAIOsmId() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getOsmId() const;
    void setOsmId(const double &osm_id);
    bool is_osm_id_Set() const;
    bool is_osm_id_Valid() const;

    QString getOsmType() const;
    void setOsmType(const QString &osm_type);
    bool is_osm_type_Set() const;
    bool is_osm_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_osm_id;
    bool m_osm_id_isSet;
    bool m_osm_id_isValid;

    QString m_osm_type;
    bool m_osm_type_isSet;
    bool m_osm_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOsmId)

#endif // OAIOsmId_H
