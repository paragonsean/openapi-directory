/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIImageTagValues.h
 *
 * 
 */

#ifndef OAIImageTagValues_H
#define OAIImageTagValues_H

#include <QJsonObject>

#include "OAITagValue.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITagValue;

class OAIImageTagValues : public OAIObject {
public:
    OAIImageTagValues();
    OAIImageTagValues(QString json);
    ~OAIImageTagValues() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getImageId() const;
    void setImageId(const qint64 &image_id);
    bool is_image_id_Set() const;
    bool is_image_id_Valid() const;

    QList<OAITagValue> getTagValues() const;
    void setTagValues(const QList<OAITagValue> &tag_values);
    bool is_tag_values_Set() const;
    bool is_tag_values_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_image_id;
    bool m_image_id_isSet;
    bool m_image_id_isValid;

    QList<OAITagValue> m_tag_values;
    bool m_tag_values_isSet;
    bool m_tag_values_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImageTagValues)

#endif // OAIImageTagValues_H
