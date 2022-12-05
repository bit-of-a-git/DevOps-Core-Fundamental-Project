CREATE TABLE IF NOT EXISTS Author(
    id INT PRIMARY KEY AUTO_INCREMENT,
	book_id INT,
    author_name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Category(
    id INT PRIMARY KEY AUTO_INCREMENT,
    cat_name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Book(
    id INT PRIMARY KEY AUTO_INCREMENT,
    book_title VARCHAR(50) NOT NULL,
    author_id INT,
    category_id INT,
    available BOOLEAN,
	FOREIGN KEY (author_id) REFERENCES Author(id),
    FOREIGN KEY (category_id) REFERENCES Category(id)
);

INSERT INTO Category (cat_name) VALUES ("Action/Adventure"), ("Biographies/Autobiographies"), ("Classics"), ("Comic Book/Graphic Novel"), ("Detective, Mystery, & True Crime"), ("Essays"), ("Fantasy"), ("Fiction"), ("History"), ("Horror"), ("Poetry"), ("Science Fiction (Sci-Fi)"), ("Self-Help"), ("Short Stories"), ("Suspense/Thrillers");