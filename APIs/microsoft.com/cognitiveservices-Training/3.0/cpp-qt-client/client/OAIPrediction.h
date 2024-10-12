/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPrediction.h
 *
 * Prediction result.
 */

#ifndef OAIPrediction_H
#define OAIPrediction_H

#include <QJsonObject>

#include "OAIBoundingBox.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBoundingBox;

class OAIPrediction : public OAIObject {
public:
    OAIPrediction();
    OAIPrediction(QString json);
    ~OAIPrediction() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIBoundingBox getBoundingBox() const;
    void setBoundingBox(const OAIBoundingBox &bounding_box);
    bool is_bounding_box_Set() const;
    bool is_bounding_box_Valid() const;

    float getProbability() const;
    void setProbability(const float &probability);
    bool is_probability_Set() const;
    bool is_probability_Valid() const;

    QString getTagId() const;
    void setTagId(const QString &tag_id);
    bool is_tag_id_Set() const;
    bool is_tag_id_Valid() const;

    QString getTagName() const;
    void setTagName(const QString &tag_name);
    bool is_tag_name_Set() const;
    bool is_tag_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIBoundingBox m_bounding_box;
    bool m_bounding_box_isSet;
    bool m_bounding_box_isValid;

    float m_probability;
    bool m_probability_isSet;
    bool m_probability_isValid;

    QString m_tag_id;
    bool m_tag_id_isSet;
    bool m_tag_id_isValid;

    QString m_tag_name;
    bool m_tag_name_isSet;
    bool m_tag_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPrediction)

#endif // OAIPrediction_H
