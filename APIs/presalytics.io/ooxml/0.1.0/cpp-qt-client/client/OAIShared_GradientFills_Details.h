/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIShared_GradientFills_Details.h
 *
 * 
 */

#ifndef OAIShared_GradientFills_Details_H
#define OAIShared_GradientFills_Details_H

#include <QJsonObject>

#include "OAIShared_FillMap_Details.h"
#include "OAIShared_GradientStops_Details.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIShared_FillMap_Details;
class OAIShared_GradientStops_Details;

class OAIShared_GradientFills_Details : public OAIObject {
public:
    OAIShared_GradientFills_Details();
    OAIShared_GradientFills_Details(QString json);
    ~OAIShared_GradientFills_Details() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAngle() const;
    void setAngle(const qint32 &angle);
    bool is_angle_Set() const;
    bool is_angle_Valid() const;

    QDateTime getDateCreated() const;
    void setDateCreated(const QDateTime &date_created);
    bool is_date_created_Set() const;
    bool is_date_created_Valid() const;

    QDateTime getDateModified() const;
    void setDateModified(const QDateTime &date_modified);
    bool is_date_modified_Set() const;
    bool is_date_modified_Valid() const;

    OAIShared_FillMap_Details getFillMap() const;
    void setFillMap(const OAIShared_FillMap_Details &fill_map);
    bool is_fill_map_Set() const;
    bool is_fill_map_Valid() const;

    QString getFillMapId() const;
    void setFillMapId(const QString &fill_map_id);
    bool is_fill_map_id_Set() const;
    bool is_fill_map_id_Valid() const;

    QList<OAIShared_GradientStops_Details> getGradientStops() const;
    void setGradientStops(const QList<OAIShared_GradientStops_Details> &gradient_stops);
    bool is_gradient_stops_Set() const;
    bool is_gradient_stops_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsPath() const;
    void setIsPath(const bool &is_path);
    bool is_is_path_Set() const;
    bool is_is_path_Valid() const;

    QString getPathType() const;
    void setPathType(const QString &path_type);
    bool is_path_type_Set() const;
    bool is_path_type_Valid() const;

    bool isRotateWithShape() const;
    void setRotateWithShape(const bool &rotate_with_shape);
    bool is_rotate_with_shape_Set() const;
    bool is_rotate_with_shape_Valid() const;

    QString getUserCreated() const;
    void setUserCreated(const QString &user_created);
    bool is_user_created_Set() const;
    bool is_user_created_Valid() const;

    QString getUserModified() const;
    void setUserModified(const QString &user_modified);
    bool is_user_modified_Set() const;
    bool is_user_modified_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_angle;
    bool m_angle_isSet;
    bool m_angle_isValid;

    QDateTime m_date_created;
    bool m_date_created_isSet;
    bool m_date_created_isValid;

    QDateTime m_date_modified;
    bool m_date_modified_isSet;
    bool m_date_modified_isValid;

    OAIShared_FillMap_Details m_fill_map;
    bool m_fill_map_isSet;
    bool m_fill_map_isValid;

    QString m_fill_map_id;
    bool m_fill_map_id_isSet;
    bool m_fill_map_id_isValid;

    QList<OAIShared_GradientStops_Details> m_gradient_stops;
    bool m_gradient_stops_isSet;
    bool m_gradient_stops_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_path;
    bool m_is_path_isSet;
    bool m_is_path_isValid;

    QString m_path_type;
    bool m_path_type_isSet;
    bool m_path_type_isValid;

    bool m_rotate_with_shape;
    bool m_rotate_with_shape_isSet;
    bool m_rotate_with_shape_isValid;

    QString m_user_created;
    bool m_user_created_isSet;
    bool m_user_created_isValid;

    QString m_user_modified;
    bool m_user_modified_isSet;
    bool m_user_modified_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIShared_GradientFills_Details)

#endif // OAIShared_GradientFills_Details_H
