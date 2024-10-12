/**
 * Highways England API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISiteTypeLayer.h
 *
 * 
 */

#ifndef OAISiteTypeLayer_H
#define OAISiteTypeLayer_H

#include <QJsonObject>

#include "OAISites.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISites;

class OAISiteTypeLayer : public OAIObject {
public:
    OAISiteTypeLayer();
    OAISiteTypeLayer(QString json);
    ~OAISiteTypeLayer() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAISites> getSites() const;
    void setSites(const QList<OAISites> &sites);
    bool is_sites_Set() const;
    bool is_sites_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAISites> m_sites;
    bool m_sites_isSet;
    bool m_sites_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISiteTypeLayer)

#endif // OAISiteTypeLayer_H
