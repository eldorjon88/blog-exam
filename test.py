from database import SessionLocal
import crud

db = SessionLocal()

# Test: user qo‘shish
user = crud.create_user(db, "test_user", "test@example.com")
print("Created User:", user.username)

# Test: user postlari
posts = crud.get_user_posts(db, user.id)
print("User posts:", posts)

# Qolgan function larni ham shu yerda test qiling






post = crud.create_post(db, user.id, "My Post", "Hello Blog!")
print("Created Post:", post.title)

# Test: comment qo‘shish
comment = crud.create_comment(db, user.id, post.id, "Nice post!")
print("Created Comment:", comment.text)

# Test: update post
updated = crud.update_post(db, post.id, "Updated Post", "Updated Body")
print("Updated:", updated.title, updated.body)

# Test: get user posts
print("User posts:", crud.get_user_posts(db, user.id))

# Test: get post comment count
print("Comment count:", crud.get_post_comment_count(db, post.id))

# Test: get latest posts
print("Latest posts:", crud.get_latest_posts(db))

# Test: search posts
print("Search results:", crud.search_posts_by_title(db, "Updated"))

# Test: paginate posts
print("Paginate:", crud.paginate_posts(db, page=1, per_page=2))
