/**
 * Face Client
 * An API for face detection, verification, and identification.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAILargeFaceList.h
 *
 * Large face list object.
 */

#ifndef OAILargeFaceList_H
#define OAILargeFaceList_H

#include <QJsonObject>

#include "OAIRecognitionModel.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAILargeFaceList : public OAIObject {
public:
    OAILargeFaceList();
    OAILargeFaceList(QString json);
    ~OAILargeFaceList() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getLargeFaceListId() const;
    void setLargeFaceListId(const QString &large_face_list_id);
    bool is_large_face_list_id_Set() const;
    bool is_large_face_list_id_Valid() const;

    OAIRecognitionModel getRecognitionModel() const;
    void setRecognitionModel(const OAIRecognitionModel &recognition_model);
    bool is_recognition_model_Set() const;
    bool is_recognition_model_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getUserData() const;
    void setUserData(const QString &user_data);
    bool is_user_data_Set() const;
    bool is_user_data_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_large_face_list_id;
    bool m_large_face_list_id_isSet;
    bool m_large_face_list_id_isValid;

    OAIRecognitionModel m_recognition_model;
    bool m_recognition_model_isSet;
    bool m_recognition_model_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_user_data;
    bool m_user_data_isSet;
    bool m_user_data_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILargeFaceList)

#endif // OAILargeFaceList_H
