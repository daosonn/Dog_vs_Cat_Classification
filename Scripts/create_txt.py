import os

def create_label_files(image_folder, output_folder, class_id=0):
    """
    Tạo các file .txt với bounding box bao phủ toàn bộ ảnh.

    Args:
    - image_folder (str): Đường dẫn đến thư mục chứa hình ảnh của chó hoặc mèo.
    - output_folder (str): Đường dẫn đến thư mục sẽ chứa các file .txt được tạo ra.
    - class_id (int): ID của lớp (0 cho chó, 1 cho mèo, tùy chỉnh theo yêu cầu).
    """

    # Tạo thư mục output nếu chưa tồn tại
    os.makedirs(output_folder, exist_ok=True)

    # Duyệt qua tất cả các file trong thư mục ảnh
    for filename in os.listdir(image_folder):
        # Kiểm tra xem file có phải là hình ảnh hay không
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Đường dẫn đầy đủ đến ảnh
            image_path = os.path.join(image_folder, filename)
            
            # Tạo nội dung cho file .txt
            label_content = f"{class_id} 0.5 0.5 1.0 1.0\n"  # Bounding box bao phủ toàn bộ ảnh

            # Đường dẫn đầy đủ đến file .txt sẽ được tạo
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_path = os.path.join(output_folder, txt_filename)

            # Ghi nội dung vào file .txt
            with open(txt_path, 'w') as f:
                f.write(label_content)

    print(f"Đã tạo xong file nhãn cho tất cả các ảnh trong thư mục '{image_folder}'.")

# Sử dụng hàm với đường dẫn đến thư mục ảnh và thư mục xuất file .txt
image_folder = r'C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Classification of cat or dog\training_set\cats'
output_folder = r'C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Classification of cat or dog\labels_cat_train'

create_label_files(image_folder, output_folder, class_id=1)  # class_id=0 cho chó, 1 cho mèo
