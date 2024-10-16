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
 * OAIImage.h
 *
 * 
 */

#ifndef OAIImage_H
#define OAIImage_H

#include <QJsonObject>

#include "OAIDicomPropertyValue.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDicomPropertyValue;

class OAIImage : public OAIObject {
public:
    OAIImage();
    OAIImage(QString json);
    ~OAIImage() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    OAIDicomPropertyValue getImageType() const;
    void setImageType(const OAIDicomPropertyValue &image_type);
    bool is_image_type_Set() const;
    bool is_image_type_Valid() const;

    OAIDicomPropertyValue getInstanceNumber() const;
    void setInstanceNumber(const OAIDicomPropertyValue &instance_number);
    bool is_instance_number_Set() const;
    bool is_instance_number_Valid() const;

    qint64 getSeriesId() const;
    void setSeriesId(const qint64 &series_id);
    bool is_series_id_Set() const;
    bool is_series_id_Valid() const;

    OAIDicomPropertyValue getSopInstanceUid() const;
    void setSopInstanceUid(const OAIDicomPropertyValue &sop_instance_uid);
    bool is_sop_instance_uid_Set() const;
    bool is_sop_instance_uid_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAIDicomPropertyValue m_image_type;
    bool m_image_type_isSet;
    bool m_image_type_isValid;

    OAIDicomPropertyValue m_instance_number;
    bool m_instance_number_isSet;
    bool m_instance_number_isValid;

    qint64 m_series_id;
    bool m_series_id_isSet;
    bool m_series_id_isValid;

    OAIDicomPropertyValue m_sop_instance_uid;
    bool m_sop_instance_uid_isSet;
    bool m_sop_instance_uid_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImage)

#endif // OAIImage_H
