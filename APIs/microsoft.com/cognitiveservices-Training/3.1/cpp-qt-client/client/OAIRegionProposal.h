/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRegionProposal.h
 *
 * 
 */

#ifndef OAIRegionProposal_H
#define OAIRegionProposal_H

#include <QJsonObject>

#include "OAIBoundingBox.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBoundingBox;

class OAIRegionProposal : public OAIObject {
public:
    OAIRegionProposal();
    OAIRegionProposal(QString json);
    ~OAIRegionProposal() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIBoundingBox getBoundingBox() const;
    void setBoundingBox(const OAIBoundingBox &bounding_box);
    bool is_bounding_box_Set() const;
    bool is_bounding_box_Valid() const;

    float getConfidence() const;
    void setConfidence(const float &confidence);
    bool is_confidence_Set() const;
    bool is_confidence_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIBoundingBox m_bounding_box;
    bool m_bounding_box_isSet;
    bool m_bounding_box_isValid;

    float m_confidence;
    bool m_confidence_isSet;
    bool m_confidence_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRegionProposal)

#endif // OAIRegionProposal_H
