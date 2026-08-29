<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đăng Ký Tư Vấn Dịch Vụ Ngân Hàng</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f4f6f9; }
        .form-card { max-width: 600px; margin: 40px auto; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        .btn-bank { background-color: #0056b3; color: white; }
        .btn-bank:hover { background-color: #003d80; color: white; }
    </style>
</head>
<body>

<div class="container">
    <div class="card form-card p-4 bg-white">
        <h3 class="text-center text-primary mb-4">DỊCH VỤ NGÂN HÀNG</h3>
        <p class="text-muted text-center mb-4">Vui lòng điền thông tin để nhận tư vấn miễn phí</p>
        
        <form id="leadForm">
            <div class="mb-3">
                <label for="fullName" class="form-label">Họ và tên <span class="text-danger">*</span></label>
                <input type="text" class="form-control" id="fullName" required placeholder="Nguyễn Văn A">
            </div>

            <div class="mb-3">
                <label for="birthYear" class="form-label">Năm sinh <span class="text-danger">*</span></label>
                <input type="number" class="form-control" id="birthYear" min="1950" max="2010" required placeholder="1995">
            </div>

            <div class="mb-3">
                <label for="phone" class="form-label">Số điện thoại <span class="text-danger">*</span></label>
                <input type="tel" class="form-control" id="phone" pattern="[0-9]{10}" required placeholder="0912345678">
            </div>

            <div class="mb-3">
                <label for="job" class="form-label">Công việc hiện tại <span class="text-danger">*</span></label>
                <input type="text" class="form-control" id="job" required placeholder="Nhân viên văn phòng, Kinh doanh tự do...">
            </div>

            <div class="mb-4">
                <label for="service" class="form-label">Dịch vụ quan tâm <span class="text-danger">*</span></label>
                <select class="form-select" id="service" required>
                    <option value="" selected disabled>-- Chọn dịch vụ --</option>
                    <option value="Mở thẻ thanh toán">Mở thẻ thanh toán</option>
                    <option value="Mở thẻ tín dụng">Mở thẻ tín dụng</option>
                    <option value="Vay mua ô tô">Vay mua ô tô</option>
                    <option value="Vay mua nhà">Vay mua nhà</option>
                    <option value="Khác">Mục khác</option>
                </select>
            </div>

            <button type="submit" class="btn btn-bank w-100 py-2">Gửi Thông Tin</button>
        </form>

        <hr class="my-4">
        <button id="exportBtn" class="btn btn-outline-success btn-sm w-100">Tải danh sách khách hàng (File Excel/CSV)</button>
    </div>
</div>

<script>
    const form = document.getElementById('leadForm');

    // Xử lý khi khách hàng ấn Gửi
    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const leadData = {
            fullName: document.getElementById('fullName').value,
            birthYear: document.getElementById('birthYear').value,
            phone: document.getElementById('phone').value,
            job: document.getElementById('job').value,
            service: document.getElementById('service').value,
            createdAt: new Date().toLocaleString('vi-VN')
        };

        // Lưu vào LocalStorage của trình duyệt
        let leads = JSON.parse(localStorage.getItem('bank_leads')) || [];
        leads.push(leadData);
        localStorage.setItem('bank_leads', JSON.stringify(leads));

        alert('Cảm ơn bạn! Thông tin đã được gửi thành công. Chúng tôi sẽ liên hệ lại sớm.');
        form.reset();
    });

    // Xuất dữ liệu ra file CSV
    document.getElementById('exportBtn').addEventListener('click', function() {
        let leads = JSON.parse(localStorage.getItem('bank_leads')) || [];
        if (leads.length === 0) {
            alert('Chưa có dữ liệu khách hàng nào!');
            return;
        }

        let csvContent = "data:text/csv;charset=utf-8,\uFEFF";
        csvContent += "Họ và tên,Năm sinh,Số điện thoại,Công việc,Dịch vụ,Thời gian đăng ký\n";

        leads.forEach(row => {
            csvContent += `"${row.fullName}","${row.birthYear}","${row.phone}","${row.job}","${row.service}","${row.createdAt}"\n`;
        });

        const encodedUri = encodeURI(csvContent);
        const link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", "danh_sach_khach_hang.csv");
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    });
</script>
</body>
</html>
